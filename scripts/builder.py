import os
import re
import markdown
import frontmatter
from datetime import datetime
from html import escape as html_escape
from email.utils import formatdate
import time

# Path configuration
POSTS_DIR = 'posts'
ASSETS_DIR = 'assets'
DIST_DIR = 'dist'
TEMPLATES = {
    'index': 'index.html',
    'post': 'post-template.html',
    'tags': 'tags.html'
}

def setup_dist():
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)
    if not os.path.exists(os.path.join(DIST_DIR, 'posts')):
        os.makedirs(os.path.join(DIST_DIR, 'posts'))
    # In a real GitHub action, assets would be copied via shell
    # But let's handle it if needed

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            path = os.path.join(POSTS_DIR, filename)
            post = frontmatter.load(path)
            
            # Use filename as slug if not provided
            slug = post.get('slug', filename.replace('.md', ''))
            
            posts.append({
                'title': post.get('title', '无题'),
                'date': post.get('date', datetime.now().strftime('%Y-%m-%d')),
                'tag': post.get('tag', '文章'),
                'excerpt': post.get('excerpt', post.content[:100] + '...'),
                'content': markdown.markdown(post.content),
                'slug': slug,
                'filename': f"{slug}.html"
            })
    
    # Sort by date descending
    posts.sort(key=lambda x: str(x['date']), reverse=True)
    return posts

def build_posts(posts):
    with open(TEMPLATES['post'], 'r', encoding='utf-8') as f:
        template = f.read()
    
    for post in posts:
        html = template.replace('<!-- POST_TITLE -->', post['title'])
        html = html.replace('<!-- POST_TAG -->', post['tag'])
        html = html.replace('<!-- POST_DATE -->', str(post['date']))
        html = html.replace('<!-- POST_CONTENT -->', post['content'])
        
        output_path = os.path.join(DIST_DIR, 'posts', post['filename'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated post: {post['filename']}")

def build_index(posts):
    with open(TEMPLATES['index'], 'r', encoding='utf-8') as f:
        index_template = f.read()
    
    post_cards = ""
    for i, post in enumerate(posts):
        # The first post gets 'featured' class
        card_class = "featured" if i == 0 else "post"
        
        card = f"""
      <article class="bento-item {card_class}">
        <h3>{post['tag']}</h3>
        <h2><a href="posts/{post['filename']}">{post['title']}</a></h2>
        <p>{post['excerpt']}</p>
        <div class="meta"><span>{post['date']}</span></div>
      </article>"""
        post_cards += card

    index_html = index_template.replace('<!-- POSTS_PLACEHOLDER -->', post_cards)
    index_html = index_html.replace('<!-- POST_COUNT -->', str(len(posts)))
    
    # Count unique tags
    tag_count = len(set(p['tag'] for p in posts))
    index_html = index_html.replace('<!-- TAG_COUNT -->', str(tag_count))
    
    with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Generated index.html")

def build_tags(posts):
    with open(TEMPLATES['tags'], 'r', encoding='utf-8') as f:
        tags_template = f.read()

    # Collect tags and their posts
    tag_map = {}
    for post in posts:
        tag = post['tag']
        if tag not in tag_map:
            tag_map[tag] = []
        tag_map[tag].append(post)

    # Sort tags by post count descending
    sorted_tags = sorted(tag_map.items(), key=lambda x: len(x[1]), reverse=True)

    # Generate tag pills
    tag_pills = ""
    for tag, tag_posts in sorted_tags:
        anchor = tag.replace(' ', '-')
        tag_pills += f'        <a href="#{anchor}" class="tag-pill">{tag} <span class="count">{len(tag_posts)}</span></a>\n'

    # Generate tag groups
    tag_groups = ""
    for tag, tag_posts in sorted_tags:
        anchor = tag.replace(' ', '-')
        post_list = ""
        for post in tag_posts:
            post_list += f"""          <div class="tag-post-item">
            <a href="posts/{post['filename']}">{post['title']}</a>
            <span class="post-date">{post['date']}</span>
          </div>
"""
        tag_groups += f"""
      <div class="tag-group" id="{anchor}">
        <div class="tag-group-header">
          <h2>{tag}</h2>
          <span class="post-count">{len(tag_posts)} 篇</span>
        </div>
        <div class="tag-post-list">
{post_list}        </div>
      </div>
"""

    tags_html = tags_template.replace('<!-- TAG_PILLS_PLACEHOLDER -->', tag_pills)
    tags_html = tags_html.replace('<!-- TAG_GROUPS_PLACEHOLDER -->', tag_groups)
    tags_html = tags_html.replace('<!-- TAG_COUNT -->', str(len(sorted_tags)))
    tags_html = tags_html.replace('<!-- POST_COUNT -->', str(len(posts)))

    with open(os.path.join(DIST_DIR, 'tags.html'), 'w', encoding='utf-8') as f:
        f.write(tags_html)
    print(f"Generated tags.html ({len(sorted_tags)} tags)")

def build_feed(posts):
    SITE_URL = 'https://edwardqiu1976.github.io'
    items = ""
    for post in posts[:20]:  # RSS 标准：最多 20 条
        # 日期转 RFC 2822 格式
        date_str = str(post['date'])
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            pub_date = formatdate(time.mktime(dt.timetuple()), localtime=True)
        except ValueError:
            pub_date = formatdate(time.time(), localtime=True)
        
        items += f"""    <item>
      <title>{html_escape(post['title'])}</title>
      <link>{SITE_URL}/posts/{html_escape(post['filename'])}</link>
      <guid isPermaLink="true">{SITE_URL}/posts/{html_escape(post['filename'])}</guid>
      <description>{html_escape(post['excerpt'])}</description>
      <pubDate>{pub_date}</pubDate>
      <category>{html_escape(post['tag'])}</category>
    </item>
"""
    
    # 最新文章日期作为 lastBuildDate
    if posts:
        try:
            dt = datetime.strptime(str(posts[0]['date']), '%Y-%m-%d')
            last_build = formatdate(time.mktime(dt.timetuple()), localtime=True)
        except ValueError:
            last_build = formatdate(time.time(), localtime=True)
    else:
        last_build = formatdate(time.time(), localtime=True)

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Edward's Blog</title>
    <link>{SITE_URL}</link>
    <description>在这里记录思考，分享探索与成长</description>
    <language>zh-CN</language>
    <lastBuildDate>{last_build}</lastBuildDate>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{items}  </channel>
</rss>"""

    with open(os.path.join(DIST_DIR, 'feed.xml'), 'w', encoding='utf-8') as f:
        f.write(feed)
    print(f"Generated feed.xml ({len(posts[:20])} items)")

if __name__ == "__main__":
    setup_dist()
    all_posts = get_posts()
    build_posts(all_posts)
    build_index(all_posts)
    build_tags(all_posts)
    build_feed(all_posts)
