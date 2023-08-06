import pandas as pd
data=pd.read_csv('movie_data.csv')

s = data['标题']
s1 = data['链接']
s2 = data['简介']
s3 = data['imdbcover']
s5= data['创建时间']
s6= data['imdblink']
s7= data['title']

t1='<div class="col-lg-3"><div class="card text-center mb-5"><div class="card-header p-0"><div class="blog-media"><div class="hoverbutton1"><img src="'
t2='" alt="Avatar" class="hoverbutton1image" style="width:100%">  <div class="hoverbutton1middle">  <a href="'
t3='" class="btn btn-outline-dark btn-sm">imdb </a>    <a href="'
t4='" class="btn btn-outline-dark btn-sm"> 豆瓣</a>  </div></div></div></div><div class="card-body px-0"><h6 class="card-title mb-2">'
t5='</h6> <small class="small text-muted"><p>'
t6='</small></div></div></div>'

t0=''
for i in range(data.shape[0]):
    t0=t0+t1+s3[i]+t2+s6[i]+t3+s1[i]+t4+s7[i]+'('+str(s2[i])+')'+t5+s[i]+'<p>'+s5[i]+t6+'\n'

# page navigation text
def navi_f(n,nn,data,mvdataname):
    if n==0:
        navi='</div><nav><center><a> < Prev | </a>'
        for j in range(int(data.shape[0]/nn)+1):
            if j==n:
                navi=navi+'<a> '+str(j+1)+' </a> '
            else:
                navi=navi+'<a href="'+mvdataname+str(j+1)+'.html'+'"> '+str(j+1)+' </a>'
        navi=navi+'<a href="'+mvdataname+str(n+2)+'.html"> | Next > </a>'+'</center></nav><div>\n'
    elif n==int(data.shape[0]/nn):
        navi='</div><nav><center><a href="'+mvdataname+str(n)+'.html"> < Prev | </a>'
        for j in range(int(data.shape[0]/nn)+1):
            if j==n:
                navi=navi+'<a> '+str(j+1)+' </a> '
            else:
                navi=navi+'<a href="'+mvdataname+str(j+1)+'.html'+'"> '+str(j+1)+' </a>'
        navi=navi+'<a> | Next > </a>'+'</center></nav><div>\n'
    else:
        navi='</div><nav><center><a href="'+mvdataname+str(n)+'.html"> < Prev | </a>'
        for j in range(int(data.shape[0]/nn)+1):
            if j==n:
                navi=navi+'<a> '+str(j+1)+' </a> '
            else:
                navi=navi+'<a href="'+mvdataname+str(j+1)+'.html'+'"> '+str(j+1)+' </a>'
        navi=navi+'<a href="'+mvdataname+str(n+2)+'.html"> | Next > </a>'+'</center></nav><div>\n'
    return navi

def Navii_f(nn,data,mvdataname):
    Navii=''
    for jj in range(int(data.shape[0]/nn)+1):
        Navii=Navii+navi_f(jj,nn,data,mvdataname)
    return Navii

mvdataname='movie_'
# mvdataname='movie_cart_'

with open('header.html', 'r',encoding="utf-8") as f:
    t_header=f.read()
    f.close()
with open('footer.html', 'r',encoding="utf-8") as f:
    t_footer=f.read()
    f.close()

nn=16
Navii=Navii_f(nn,data,mvdataname)

for j in range(int(data.shape[0]/nn)+1):
    if j==int(data.shape[0]/nn):
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(data.shape[0]-int(data.shape[0]/nn)*nn):
                f.write(t0.splitlines()[nn*j+i])
            f.write(Navii.splitlines()[j])
            f.write(t_footer)
    else:
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(nn):
                f.write(t0.splitlines()[nn*j+i])
            f.write(Navii.splitlines()[j])
            f.write(t_footer)

datadoc=data.loc[data['Tag/Documentary'] == 1]
s = datadoc['标题']
s1 = datadoc['链接']
s2 = datadoc['简介']
s3 = datadoc['imdbcover']
s5= datadoc['创建时间']
s6= datadoc['imdblink']
s7= datadoc['title']
t0=''
for i in datadoc.index:
    t0=t0+t1+s3[i]+t2+s6[i]+t3+s1[i]+t4+s7[i]+'('+str(s2[i])+')'+t5+s[i]+'<p>'+s5[i]+t6+'\n'

mvdataname='movie_doc_'

nn=16
Navii=Navii_f(nn,datadoc,mvdataname)

for j in range(int(datadoc.shape[0]/nn)+1):
    if j==int(datadoc.shape[0]/nn):
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(datadoc.shape[0]-int(datadoc.shape[0]/nn)*nn):
                f.write(t0.splitlines()[nn*j+i])
            f.write(Navii.splitlines()[j])
            f.write(t_footer)
    else:
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(nn):
                f.write(t0.splitlines()[nn*j+i])
            f.write(Navii.splitlines()[j])
            f.write(t_footer)

datadoc=data.loc[data['Tag/TV'] == 1]
s = datadoc['标题']
s1 = datadoc['链接']
s2 = datadoc['简介']
s3 = datadoc['imdbcover']
s5= datadoc['创建时间']
s6= datadoc['imdblink']
s7= datadoc['title']
t0=''
for i in datadoc.index:
    t0=t0+t1+s3[i]+t2+s6[i]+t3+s1[i]+t4+s7[i]+'('+str(s2[i])+')'+t5+s[i]+'<p>'+s5[i]+t6+'\n'

mvdataname='movie_TV_'

nn=16
Navii=Navii_f(nn,datadoc,mvdataname)

for j in range(int(datadoc.shape[0]/nn)+1):
    if j==int(datadoc.shape[0]/nn):
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(datadoc.shape[0]-int(datadoc.shape[0]/nn)*nn):
                f.write(t0.splitlines()[nn*j+i])
            f.write(Navii.splitlines()[j])
            f.write(t_footer)
    else:
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(nn):
                f.write(t0.splitlines()[nn*j+i])
            f.write(Navii.splitlines()[j])
            f.write(t_footer)
