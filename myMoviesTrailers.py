import movie
# import os
import fresh_tomatoes

shediao = movie.Movie('shediao1983', 'a kongfu movie and TV series released in 1983',
                           'https://r3.ykimg.com/0516000051C69D6C6758391DB70BF877',
                           'https://v.youku.com/v_show/id_XMjI3MDQ1MTU2.html')

CZ12 = movie.Movie('CZ12', 'A kungfu movie by Jack Chen', 'https://i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/o/opq82bnh2jjjlha.jpg', 'https://v.qq.com/x/cover/opq82bnh2jjjlha/h00112web9l.html')
KungFuYoga = movie.Movie('Kung Fu Yoga', 'A kungfu movie by Jack Chen in 2017', 'https://puui.qpic.cn/vcover_vt_pic/0/cmv67rzhrf5s5r31479344822/0', 'https://v.qq.com/x/cover/cmv67rzhrf5s5r3/q0370sukc42.html')
TheForeigner = movie.Movie('The Foreigner', 'A kungfu movie by Jack Chen in 2017', 'https://i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/u/u4s2zisluorvkgt.jpg', 'https://v.qq.com/x/cover/u4s2zisluorvkgt/r030691rquh.html')
PersonalTailor = movie.Movie('Personal Tailor', 'A comedy directed by Feng Xiaogang', 'https://i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/o/o4bmve7g33cqqr9.jpg', 'https://v.qq.com/x/cover/o4bmve7g33cqqr9/b0013df9o0l.html')

movies = [
    shediao,
    CZ12,
    KungFuYoga,
    TheForeigner,
    PersonalTailor
]

fresh_tomatoes.open_movies_page(movies)
