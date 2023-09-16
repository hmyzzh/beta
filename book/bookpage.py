import pandas as pd
mvdataname='book_'
data1=pd.read_csv('book_data1.csv')
s = data1['ctitle']
s1 = data1['Neodb_link']
s2 = data1['author']
s3 = data1['Cover1']
s5= data1['Create_time']
s6= data1['db_link']
s7= data1['ctitle']
t1='<div class="col-lg-3"><div class="card text-center mb-5"><div class="card-header p-0"><div class="blog-media"><div class="hoverbutton1"><img src="'
t2='" alt="Avatar" class="hoverbutton1image" style="width:100%">  <div class="hoverbutton1middle">  <a href="'
t3='" class="btn btn-outline-dark btn-sm">豆瓣 </a>    <a href="'
t4='" class="btn btn-outline-dark btn-sm">NeoDB</a>  </div></div></div></div><div class="card-body px-0"><h6 class="card-title mb-2">'
t5='</h6> <small class="small text-muted"><p>'
t6='</small></div></div></div>'
t0=''
for i in range(data1.shape[0]):
    t0=t0+t1+s3[i]+t2+s6[i]+t3+s1[i]+t4+s7[i]+t5+s2[i]+'<p>'+s5[i]+t6+'\n'
    
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
with open('header_book.html', 'r',encoding="utf-8") as f:
    t_header=f.read()
    f.close()
with open('footer.html', 'r',encoding="utf-8") as f:
    t_footer=f.read()
    f.close()

nn=16
Navii=Navii_f(nn,data1,mvdataname)

for j in range(int(data1.shape[0]/nn)+1):
    if j==int(data1.shape[0]/nn):
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(data1.shape[0]-int(data1.shape[0]/nn)*nn):
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

mvdataname='book_ing_'
data1=pd.read_csv('book_data2.csv')
s = data1['ctitle']
s1 = data1['Neodb_link']
s2 = data1['author']
s3 = data1['Cover1']
s5= data1['Create_time']
s6= data1['db_link']
s7= data1['ctitle']
t1='<div class="col-lg-3"><div class="card text-center mb-5"><div class="card-header p-0"><div class="blog-media"><div class="hoverbutton1"><img src="'
t2='" alt="Avatar" class="hoverbutton1image" style="width:100%">  <div class="hoverbutton1middle">  <a href="'
t3='" class="btn btn-outline-dark btn-sm">豆瓣 </a>    <a href="'
t4='" class="btn btn-outline-dark btn-sm">NeoDB</a>  </div></div></div></div><div class="card-body px-0"><h6 class="card-title mb-2">'
t5='</h6> <small class="small text-muted"><p>'
t6='</small></div></div></div>'
t0=''
for i in range(data1.shape[0]):
    t0=t0+t1+s3[i]+t2+s6[i]+t3+s1[i]+t4+s7[i]+t5+s2[i]+'<p>'+s5[i]+t6+'\n'
    
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
with open('header_book.html', 'r',encoding="utf-8") as f:
    t_header=f.read()
    f.close()
with open('footer.html', 'r',encoding="utf-8") as f:
    t_footer=f.read()
    f.close()

nn=16
Navii=Navii_f(nn,data1,mvdataname)

for j in range(int(data1.shape[0]/nn)+1):
    if j==int(data1.shape[0]/nn):
        with open(mvdataname+str(j+1)+'.html', 'w',encoding="utf-8") as f:   
            f.write(t_header)
            for i in range(data1.shape[0]-int(data1.shape[0]/nn)*nn):
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