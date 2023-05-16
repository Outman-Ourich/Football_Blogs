from django.shortcuts import render
from datetime import date
from django.http import HttpResponseNotFound 
from django.template.loader import render_to_string

all_posts = [
    {
    "slug" : "cr7",
    "image":"cr7.jpg",
    "author":"Outman",
    "date": date(2022 , 12, 18),
    "title": "Cristiano the machine",
    "excerpt" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta rem pariatur quasi mollitia? A accusantium nisi corporis rem. Doloribus suscipit corrupti ab incidunt porro, quod fugit voluptas vitae itaque consequatur."
    ,"content" : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas dignissimos possimus similique sunt facilis labore impedit. Quasi iste, accusamus quis, voluptas sit ab impedit a excepturi ullam id commodi soluta.
Modi excepturi ipsum eum eligendi, sit dolor. Dolore alias, repellat vitae repellendus itaque explicabo eligendi, aliquam ullam in error impedit perspiciatis ex, expedita neque consequatur sint unde atque? Deserunt, voluptates.
Cupiditate sunt consectetur quasi culpa a adipisci voluptatum, quidem nostrum, harum nihil dicta eaque fuga. Perferendis sequi, eos odio, voluptate molestiae recusandae voluptas eaque cumque laudantium nisi quaerat dignissimos. Repellendus."""
    },
        {
    "slug" : "njr",
    "image":"njr.jpg",
    "author":"Outman",
    "date": date(2022 , 12, 18),
    "title": "Neymar the magician",
    "excerpt" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta rem pariatur quasi mollitia? A accusantium nisi corporis rem. Doloribus suscipit corrupti ab incidunt porro, quod fugit voluptas vitae itaque consequatur."
    ,"content" : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas dignissimos possimus similique sunt facilis labore impedit. Quasi iste, accusamus quis, voluptas sit ab impedit a excepturi ullam id commodi soluta.
Modi excepturi ipsum eum eligendi, sit dolor. Dolore alias, repellat vitae repellendus itaque explicabo eligendi, aliquam ullam in error impedit perspiciatis ex, expedita neque consequatur sint unde atque? Deserunt, voluptates.
Cupiditate sunt consectetur quasi culpa a adipisci voluptatum, quidem nostrum, harum nihil dicta eaque fuga. Perferendis sequi, eos odio, voluptate molestiae recusandae voluptas eaque cumque laudantium nisi quaerat dignissimos. Repellendus."""
    },
        {
    "slug" : "rl9",
    "image":"lewa.jpg",
    "author":"Outman",
    "date": date(2022 , 12, 18),
    "title": "Robert Lewandowski the best N°9",
    "excerpt" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta rem pariatur quasi mollitia? A accusantium nisi corporis rem. Doloribus suscipit corrupti ab incidunt porro, quod fugit voluptas vitae itaque consequatur."
    ,"content" : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas dignissimos possimus similique sunt facilis labore impedit. Quasi iste, accusamus quis, voluptas sit ab impedit a excepturi ullam id commodi soluta.
Modi excepturi ipsum eum eligendi, sit dolor. Dolore alias, repellat vitae repellendus itaque explicabo eligendi, aliquam ullam in error impedit perspiciatis ex, expedita neque consequatur sint unde atque? Deserunt, voluptates.
Cupiditate sunt consectetur quasi culpa a adipisci voluptatum, quidem nostrum, harum nihil dicta eaque fuga. Perferendis sequi, eos odio, voluptate molestiae recusandae voluptas eaque cumque laudantium nisi quaerat dignissimos. Repellendus."""
    },
     {
    "slug" : "IZ",
    "image":"zlatan.jpg",
    "author":"Outman",
    "date": date(2022 , 12, 11),
    "title": "Zlatan Ibrahimovic the lion",
    "excerpt" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta rem pariatur quasi mollitia? A accusantium nisi corporis rem. Doloribus suscipit corrupti ab incidunt porro, quod fugit voluptas vitae itaque consequatur."
    ,"content" : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas dignissimos possimus similique sunt facilis labore impedit. Quasi iste, accusamus quis, voluptas sit ab impedit a excepturi ullam id commodi soluta.
Modi excepturi ipsum eum eligendi, sit dolor. Dolore alias, repellat vitae repellendus itaque explicabo eligendi, aliquam ullam in error impedit perspiciatis ex, expedita neque consequatur sint unde atque? Deserunt, voluptates.
Cupiditate sunt consectetur quasi culpa a adipisci voluptatum, quidem nostrum, harum nihil dicta eaque fuga. Perferendis sequi, eos odio, voluptate molestiae recusandae voluptas eaque cumque laudantium nisi quaerat dignissimos. Repellendus."""
    }, {
    "slug" : "dimaria",
    "image":"dimaria.jpg",
    "author":"Outman",
    "date": date(2022 , 12, 11),
    "title": "Angel Di Maria the man of finals",
    "excerpt" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta rem pariatur quasi mollitia? A accusantium nisi corporis rem. Doloribus suscipit corrupti ab incidunt porro, quod fugit voluptas vitae itaque consequatur."
    ,"content" : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas dignissimos possimus similique sunt facilis labore impedit. Quasi iste, accusamus quis, voluptas sit ab impedit a excepturi ullam id commodi soluta.
Modi excepturi ipsum eum eligendi, sit dolor. Dolore alias, repellat vitae repellendus itaque explicabo eligendi, aliquam ullam in error impedit perspiciatis ex, expedita neque consequatur sint unde atque? Deserunt, voluptates.
Cupiditate sunt consectetur quasi culpa a adipisci voluptatum, quidem nostrum, harum nihil dicta eaque fuga. Perferendis sequi, eos odio, voluptate molestiae recusandae voluptas eaque cumque laudantium nisi quaerat dignissimos. Repellendus."""
    }, {
    "slug" : "wr10",
    "image":"rooney.jpg",
    "author":"Outman",
    "date": date(2022 , 12, 13),
    "title": "Wayne Rooney the golden boy",
    "excerpt" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta rem pariatur quasi mollitia? A accusantium nisi corporis rem. Doloribus suscipit corrupti ab incidunt porro, quod fugit voluptas vitae itaque consequatur."
    ,"content" : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas dignissimos possimus similique sunt facilis labore impedit. Quasi iste, accusamus quis, voluptas sit ab impedit a excepturi ullam id commodi soluta.
Modi excepturi ipsum eum eligendi, sit dolor. Dolore alias, repellat vitae repellendus itaque explicabo eligendi, aliquam ullam in error impedit perspiciatis ex, expedita neque consequatur sint unde atque? Deserunt, voluptates.
Cupiditate sunt consectetur quasi culpa a adipisci voluptatum, quidem nostrum, harum nihil dicta eaque fuga. Perferendis sequi, eos odio, voluptate molestiae recusandae voluptas eaque cumque laudantium nisi quaerat dignissimos. Repellendus."""
    },
    
]
def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/main_page.html",{
        "posts" : latest_posts
    })
def posts(request):
    """ sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:] """
    return render(request,"blog/all-posts.html",{
        "posts" : all_posts
    })
def post(request,slug):
    identified_post= next(post for post in all_posts if post['slug']== slug)
    return render(request,"blog/post.html",{
        "post" : identified_post
    })

