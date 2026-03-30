import os
import re
import markdown
import frontmatter
from datetime import datetime

# Path configuration
POSTS_DIR = 'posts'
ASSETS_DIR = 'assets'
DIST_DIR = 'dist'
TEMPLATES = {
    'index': 'index.html',
    'post': 'post-template.html'
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
    
    # Fix asset paths in dist/index.html
    # (Since index is in root of dist, assets/style.css is correct)
    
    with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Generated index.html")

if __name__ == "__main__":
    setup_dist()
    all_posts = get_posts()
    build_posts(all_posts)
    build_index(all_posts)
