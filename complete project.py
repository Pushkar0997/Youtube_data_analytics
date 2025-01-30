import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv("search.csv")
df3=pd.read_csv("new1.csv",index_col="weeks")

def bootup():
    print("type 'youtube()' ")
    print()
    jj=input("")
    print()
    if jj=="youtube()":
        youtube()
    else:
        print("wrong command prompted")
        print()
        input("press enter to retry")
        print()
        bootup()
        
def youtube():

    def ur():        
            if ai12==0:
                print(df1.loc[ai12:ai12+4,])
                input("press enter to go back")
                home()
            elif ai12==1:
                print(df1.loc[5:9,])
                input("press enter to go back")
                home()
            elif ai12==2:
                print(df1.loc[10:14,])
                input("press enter to go back")
                home()
            elif ai12==3:
                print(df1.loc[15:19,])
                input("press enter to go back")
                home()
            elif ai12==4:
                print(df1.loc[20:,])
                input("press enter to go back")
                home()
            else:
                print('new user data not available')
                input("press enter to go back")
                home()
    def anlyts():
        print('''
(type the alphabet for transversing between pages)

|--------------------|
|a.likes hit         |
|b.length trend      | 
|c.views got         |
|--------------------|''')
        w1=input("enter your choice")
        if w1=="a":
            k=0
            while True:
                if k>24:
                    print("no data available")
                    print()
                    home()
                if df1.channel[k]==a123:
                    a=[df1.date[k],df1.date[k+1],df1.date[k+2],df1.date[k+3],df1.date[k+4]]
                    b=[df1.likes[k],df1.likes[k+1],df1.likes[k+2],df1.likes[k+3],df1.likes[k+4]]
                    plt.plot(a,b,color="r",linestyle="solid",marker="+",markeredgecolor="b")
                    plt.xlabel("date")
                    plt.ylabel("likes")
                    plt.grid(True)
                    plt.show()
                    home()
                else:
                    k=k+5
        elif w1=="c":
            k=0
            while True:
                if k>24:
                    print("no data available")
                    print()
                    home()
                if df1.channel[k]==a123:
                    a=[df1.date[k],df1.date[k+1],df1.date[k+2],df1.date[k+3],df1.date[k+4]]
                    b=[df1.views[k],df1.views[k+1],df1.views[k+2],df1.views[k+3],df1.views[k+4]]
                    plt.plot(a,b,color="g",linestyle="dotted",marker="o",markeredgecolor="m")
                    plt.xlabel("date")
                    plt.ylabel("views")
                    plt.grid(True)
                    plt.show()
                    home()
                else:
                    k=k+5
        elif w1=="b":
            k=0
            while True:
                if k>24:
                    print("no data available")
                    print()
                    home()
                if df1.channel[k]==a123:
                    a=[df1.video[k],df1.video[k+1],df1.video[k+2],df1.video[k+3],df1.video[k+4]]
                    b=[df1.length[k],df1.length[k+1],df1.length[k+2],df1.length[k+3],df1.length[k+4]]
                    plt.plot(a,b,color="b",linestyle="dashed",marker="D",markeredgecolor="r")
                    plt.xlabel("video name")
                    plt.ylabel("length (in mins)")
                    plt.grid(True)
                    plt.show()
                    home()
                else:
                    k=k+5
    def search():
            print("type 'back' to return") 
            choi=input("search video to display :  ")
            k=0
            if choi=="back":
                print()
                home()
            else:
                while True:
                    if k > 24:
                        print("no video available")
                        input("press enter to continue")
                        print()
                        search()
                        break
                    else:
                        if df1.video[k]==choi:
                            print(df1.loc[k:k,:])
                            print()
                            input("press enter to continue")
                            print()
                            search()
                        else:
                            k=k+1

    def channel():
            k=0
            a=[df1.channel[k],df1.channel[k+5],df1.channel[k+10],df1.channel[k+15],df1.channel[k+20]]
            b=[df1.subscribers[k],df1.subscribers[k+5],df1.subscribers[k+10],df1.subscribers[k+15],df1.subscribers[k+20]]
            plt.bar(a,b,color=['red','b','g','k'],hatch="*",edgecolor="y")
            plt.xlabel("channels")
            plt.ylabel("subscribers")
            plt.show()
            print()
            home()

    def covid():
            print("type 'back' to return") 
            choj=input("enter first video to display :  ")
            if choj=="back":
                print()
                home()
            else:
                chok=input("enter second video to display :  ")
                k=0
                q=0
                if chok=="back":
                    print()
                    home()
                else:
                    while True:
                        if k>24:
                            print("first video doesnt exist")
                            input("press enter to continue")
                            print()
                            covid()
                        if df1.video[k]==choj:
                            if q > 24:
                                print("second video doesnt exist")
                                input("press enter to continue")
                                print()
                                covid()
                            if df1.video[q]==chok:
                                k1=[df1.subscribers[k],df1.likes[k]]
                                q1=[df1.subscribers[q],df1.likes[q]]
                                info=["subscribers","likes"]
                                x=np.arange(len(info))
                                plt.bar(info,k1,width=0.25,label=choj)
                                plt.bar(x+0.26,q1,width=0.25,label=chok)
                                plt.legend(loc="upper right")
                                plt.show()
                                print()
                                covid()
                            else:
                                q=q+1
                        else:
                            k=k+1

    def cog():
            print("type 'back' to return") 
            choi=input("search genre to display :  ")
            k=0
            if choi=="back":
                print()
                home()
            else:
                while True:
                    if k > 24:
                        print("no such genre exists")
                        input("press enter to continue")
                        print()
                        cog()
                        break
                    else:
                        if df1.genre[k]==choi:
                            print(df1.loc[k:k+4,:])
                            input("press enter to continue")
                            print()
                            cog()
                            break
                        else:
                            k=k+1

    def dat():
        print('''
(type the alphabet for transversing between pages)

|--------------------|
|a.weeks wise        |
|b.month wise        | 
|--------------------|''')
        e1=input("enter your choice  : ")
        if e1=='a':
            if ai12==0:
                print(t1.T)
                input("press enter to go back")
                home()
            elif ai12==1:
                print(t2.T)
                input("press enter to go back")
                home()
            elif ai12==2:
                print(t3.T)
                input("press enter to go back")
                home()
            elif ai12==3:
                print(t4.T)
                input("press enter to go back")
                home()
            elif ai12==4:
                print(t5.T)
                input("press enter to go back")
                home()
            else:
                print('new user data not available')
                input("press enter to go back")
                home()
        elif e1=="b":
            print()
            print("format for month like for 'January' write 'jan' ")
            print()
            y=input("enter month for which you want data to diplayed  : ")
            if y=='jan':
             if ai12==0:
                print(m1[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m1[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m1[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m1[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m1[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            elif y=='feb':
             if ai12==0:
                print(m2[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m2[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m2[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m2[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m2[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='mar':
             if ai12==0:
                print(m3[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m3[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m3[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m3[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m3[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()    
            if y=='apr':
             if ai12==0:
                print(m4[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m4[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m4[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m4[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m4[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='may':
             if ai12==0:
                print(m5[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m5[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m5[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m5[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m5[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='jun':
             if ai12==0:
                print(m6[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m6[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m6[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m6[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m6[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='jul':
             if ai12==0:
                print(m7[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m7[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m7[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m7[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m7[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='aug':
             if ai12==0:
                print(m8[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m8[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m8[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m8[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m8[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='sep':
             if ai12==0:
                print(m9[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m9[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m9[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m9[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m9[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='oct':
             if ai12==0:
                print(m10[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m10[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m10[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m10[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m10[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='nov':
             if ai12==0:
                print(m11[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m11[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m11[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m11[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m11[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            if y=='dec':
             if ai12==0:
                print(m12[0:8])
                input("press enter to go back")
                home()
             elif ai12==1:
                print(m12[8:16])
                input("press enter to go back")
                home()
             elif ai12==2:
                print(m12[16:24])
                input("press enter to go back")
                home()
             elif ai12==3:
                print(m12[24:32])
                input("press enter to go back")
                home()
             elif ai12==4:
                print(m12[32:40])
                input("press enter to go back")
                home()
             else:
                print('new user data not available')
                input("press enter to go back")
                home()
            else:
                print("please enter month in valid fromat")
                dat()

    def perf():        
            if ai12==0:
                df3.iloc[:,0:4].plot()
                plt.show()
                input("press enter to go back")
                home()
            elif ai12==1:
                df3.iloc[:,8:12].plot()
                plt.show()
                input("press enter to go back")
                home()
            elif ai12==2:
                df3.iloc[:,16:20].plot()
                plt.show()
                input("press enter to go back")
                home()
            elif ai12==3:
                df3.iloc[:,24:28].plot()
                plt.show()
                input("press enter to go back")
                home()
            elif ai12==4:
                df3.iloc[:,32:36].plot()
                plt.show()
                input("press enter to go back")
                home()
            else:
                print('new user data not available')
                input("press enter to go back")
                home()

    def diff():
        print('''
(type the alphabet for transversing between pages)

|--------------------|
|a.crisp summary     |
|b.likes gain        |
|c.subscribers gain  |
|d.views got         |
|e.return to home    |
|--------------------|''')
        u1=input("enter your choice")
        if u1=="a":
            df3.plot(kind="bar")
            plt.show()
            home()
        elif u1=="b":
            print()
            print("type 1 for week wise and 2 for month wise trend")
            print()
            u2=input("enter your choice  : ")
            if u2=="1":
                df3.iloc[:,[1,9,17,25,33]].plot(marker="<")
                plt.show()
                home()
            if u2=="2":
                print("type the name of month in the same format as used before")
                u3=input("enter month")
                if u3=="jan":
                   df3.iloc[0:4,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="feb":
                   df3.iloc[4:8,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="mar":
                   df3.iloc[8:12,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="apr":
                   df3.iloc[12:16,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="may":
                   df3.iloc[16:20,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="jun":
                   df3.iloc[20:25,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="jul":
                   df3.iloc[25:30,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="aug":
                   df3.iloc[30:34,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="sep":
                   df3.iloc[34:39,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="oct":
                   df3.iloc[39:43,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="nov":
                   df3.iloc[43:47,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="dec":
                   df3.iloc[47:,[1,9,17,25,33]].plot(kind="bar")
                   plt.show()
                   diff()
                else:
                    print("please enter month in valid format")
                    diff()
        elif u1=="c":
            print()
            print("type 1 for week wise and 2 for month wise trend")
            print()
            u4=input("enter your choice  : ")
            if u4=="1":
                df3.iloc[:,[0,8,16,24,32]].plot(marker="^")
                plt.show()
                home()
            if u4=="2":
                print("type the name of month in the same format as used before")
                u3=input("enter month")
                if u3=="jan":
                   df3.iloc[0:4,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="feb":
                   df3.iloc[4:8,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="mar":
                   df3.iloc[8:12,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="apr":
                   df3.iloc[12:16,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="may":
                   df3.iloc[16:20,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="jun":
                   df3.iloc[20:25,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="jul":
                   df3.iloc[25:30,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="aug":
                   df3.iloc[30:34,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="sep":
                   df3.iloc[34:39,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="oct":
                   df3.iloc[39:43,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="nov":
                   df3.iloc[43:47,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="dec":
                   df3.iloc[47:,[0,8,16,24,32]].plot(kind="bar")
                   plt.show()
                   diff()
                else:
                    print("please enter month in valid format")
                    diff()
        elif u1=="d":
            print()
            print("type 1 for week wise and 2 for month wise trend")
            print()
            u4=input("enter your choice  : ")
            if u4=="1":
                df3.iloc[:,[3,11,19,27,35]].plot(marker="^")
                plt.show()
                home()
            if u4=="2":
                print("type the name of month in the same format as used before")
                u3=input("enter month")
                if u3=="jan":
                   df3.iloc[0:4,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="feb":
                   df3.iloc[4:8,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="mar":
                   df3.iloc[8:12,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="apr":
                   df3.iloc[12:16,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="may":
                   df3.iloc[16:20,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="jun":
                   df3.iloc[20:25,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="jul":
                   df3.iloc[25:30,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="aug":
                   df3.iloc[30:34,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="sep":
                   df3.iloc[34:39,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="oct":
                   df3.iloc[39:43,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="nov":
                   df3.iloc[43:47,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                elif u3=="dec":
                   df3.iloc[47:,[3,11,19,27,35]].plot(kind="bar")
                   plt.show()
                   diff()
                else:
                    print("please enter month in valid format")
                    diff()
        elif u1=="e":
            input("presss enter to exit")
            home()

    def genre():
        print('''
(type the alphabet for transversing between pages)

|--------------------------|
|a.trending this month     |
|b.search for genre        |
|c.view report             |
|d.return to home          |
|--------------------------|''')
        i1=input("enter your choice")
        if i1=="a":
                print("type the name of month in the same format as used before")
                i3=input("enter month")
                if i3=="jan":
                    a9=max(df3.iloc[0:4,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="feb":
                    a9=max(df3.iloc[4:8,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="mar":
                    a9=max(df3.iloc[8:12,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="apr":
                    a9=max(df3.iloc[12:16,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="may":
                    a9=max(df3.iloc[16:20,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    print()
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="jun":
                    a9=max(df3.iloc[20:25,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    print()
                    for i in df3[a9]:
                       a1.append(i)
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="jul":
                    a9=max(df3.iloc[25:30,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="aug":
                    a9=max(df3.iloc[30:34,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="sep":
                    a9=max(df3.iloc[34:39,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="oct":
                    a9=max(df3.iloc[39:43,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="nov":
                    a9=max(df3.iloc[43:47,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                elif i3=="dec":
                    a9=max(df3.iloc[47:,40:])
                    print()
                    print("GENRE TRENDING THIS MONTH IS",a9)
                    a1=[]
                    for i in df3[a9]:
                       a1.append(i)
                    print()
                    print("the no. of people who searched this genre is ",max(a1))
                    genre()
                else:
                    print("please enter month in valid format")
                    genre()
        elif i1=="b":
            p1=input("enter the genre to be searched  : ")
            if p1=="action":

                print(df3["action"])
                print("the analysis of this genre is jan month is shown in graph  ")
                df3.iloc[0:4,40].plot(kind="hist",hatch="|",color="blue")
                plt.show()
                genre()
            elif p1=="music":
                print(df3["music"])
                print("the analysis of this genre is mar month is shown in graph  ")
                df3.iloc[8:12,42].plot(kind="hist",hatch="|",color="blue",histtype="step")
                plt.show()
                genre()
            elif p1=="lifestyle":
                print(df3["lifestyle"])
                print("the analysis of this genre is apr month is shown in graph  ")
                df3.iloc[12:16,41].plot(kind="hist",hatch="|",color="red",histtype="step")
                plt.show()
                genre()
            elif p1=="entertainment":
                print(df3["entertainment"])
                print("the analysis of this genre is jun month is shown in graph  ")
                df3.iloc[20:25,43].plot(kind="hist",hatch="^",color="blue",histtype="step")
                plt.show()
                genre()
            elif p1=="education":
                print(df3["education"])
                print("the analysis of this genre is aug month is shown in graph  ")
                df3.iloc[30:34,44].plot(kind="hist",hatch="|",color="blue",histtype="bar",cumulative=True)
                plt.show()
                genre()
            else:
                print("please enter a valid genre")
        elif i1=="c":
            print("the reports for first 4 weeks are shown here  ")
            print("type a no in rangr 0 to 3 to select the week whose report you want to see")
            j1=input("enter the no")
            if j1=="0":
                expl=[0.5,0.2,1.1,0,0]
                colr=['red','cyan','pink','yellow','silver']
                df3.iloc[0,40:].plot(kind="pie",explode=expl,colors=colr,autopct="%5.2f%%")
                plt.show()
                genre()
            elif j1=="1":
                expl=[0.5,0.2,1.4,0,0]
                colr=['red','cyan','pink','yellow','silver']
                df3.iloc[1,40:].plot(kind="pie",explode=expl,colors=colr,autopct="%5.2f%%")
                plt.show()
                genre()
            elif j1=="2":
                expl=[0,0,1.1,0,0]
                colr=['red','cyan','pink','yellow','silver']
                df3.iloc[0,40:].plot(kind="pie",explode=expl,colors=colr,autopct="%5.2f%%")
                plt.show()
                genre()
            elif j1=="3":
                expl=[0.5,0,0,0,0]
                colr=['red','cyan','pink','yellow','silver']
                df3.iloc[0,40:].plot(kind="pie",explode=expl,colors=colr,autopct="%5.2f%%")
                plt.show()
                genre()
            else:
                print("please enter a valid no")
        if i1=="d":
            home()
    def logout():
            print("logout successful")
            print()
            print("if you want to login again type 1")
            print()
            print("if you want to exit type 2")
            l1=input("enter your choice")
            if l1=="1":
                bootup()
            elif l1=="2":
                print(" thankyou, please return back soon :)")
                exit()
            else:
                print("please enter a valid no")
            
    def home():
        print('''

============================================================================================================================================================================================    

                                                                  hh         oooooooo    mm       mm    eeeeeee
                                                                  hh         oooooooo    mmmm    mmm    eeeeeee
                                                                  hh         oo    oo    mm mm mm mm    ee
                                                                  hh         oo    oo    mm   mm  mm    eeeeeee
                                                                  hhhhhhh    oo    oo    mm       mm    eeeeeee
                                                                  hh   hh    oo    oo    mm       mm    ee
                                                                  hh   hh    oooooooo    mm       mm    eeeeeee
                                                                  hh   hh    oooooooo    mm       mm    eeeeeee
         
============================================================================================================================================================================================


(type the option for transversing between pages (e.g "1a"))
                                                                                       _
______________________________________________________________________________________|-|___________________________________________________________________________________________________
|                                                                                     |-|                                                                                                  |
|                  PROCEED WITH OLD DATA                                              |-|                PROCEED WITH THIS YEAR'S NEW DATA                                                 |
|_____________________________________________________________________________________|-|__________________________________________________________________________________________________|
| 1A. YOUR  CHANNEL VIDEOS                                                            |-|  2a. YOUR VIDEOS(LOOK FOR YOUR DATA)                                                             |
| 1b. YOUR CHANNEL ANALYTICS                                                          |-|  2b.YOUR ANALYTICS(ANALYSE YOUR CHANNEL PERFORMANCE)                                             |
| 1c. SEARCH VIDEOS(ANY CHANNEL)                                                      |-|  2c.CHANNEL ANALYTICS(ANALYSE DIFFERENT CHANNELS)                                                |
| 1d. CHANNEL ANALYTICS(COMPARE SUBSCRIBERS FROM DIFF CHANNEL)                        |-|  2d.SEARCH VIDEOS BY GENRE                                                                       |
| 1e. COMPARE VIDEOS(FROM ANY CHANNEL)                                                |-|  2e.LOOK FOR WHOLE DATA                                                                          |
| 1f. SEARCH VIDEOS BY GENRE                                                          |-|                                                                                                  |
|-------------------------------------------------------------------------------------|-|--------------------------------------------------------------------------------------------------|
|                                                                             TYPE 'O' FOR LOGOUT                                                                                          |
|-------------------------------------------------------------------------------------|_|--------------------------------------------------------------------------------------------------|
                                                                                       
  ''')
        print()
        print()
        no=input("choose your choice  :  ")
        print()
        print()
        if no=="1a":
            ur()
        if no=="1b":
            anlyts()
        if no=="1c":
            search()
        if no=="1d":
            channel()
        if no=="1e":
            covid()
        if no=="1f":
            cog()
        if no=="2a":
            dat()
        if no=="2b":
            perf()
        if no=="2c":
            diff()
        if no=="2d":
            genre()
        if no=="2e":
            print(df3)
            print()
            input("press enter to exit")
            print()
            home()
        if no=="o":
            logout()
        else:
            print("invalid option")
            home()

    print('''
welcome to.......

        ╔════════╦╦═══╦╦═══╗
        ║╔╦╦═╦╗╔╦╣╠╦╗╔╣╚╦═╗║
        ║║║║║║╚╝╠╗╔╣╚╝║║║╩╣║
        ║╠╗╠═╩══╝╚═╩══╩═╩═╝║
        ╚╩═╩═══════════════╝''')
    print()
    print()
    print()
   
    t1=df3.iloc[:,0:8]#arjun
    t2=df3.iloc[:,8:16]#bright
    t3=df3.iloc[:,16:24]#marsh
    t4=df3.iloc[:,24:32]#dude
    t5=df3.iloc[:,32:40]#edu
    t6=df3.iloc[:,40:]#genre
    m1=df3.iloc[[0,1,2,3]].sum(axis=0)
    m2=df3.iloc[[4,5,6,7]].sum(axis=0)
    m3=df3.iloc[[8,9,10,11,12]].sum(axis=0)
    m4=df3.iloc[[13,14,15,16]].sum(axis=0)
    m5=df3.iloc[[17,18,19,20,21]].sum(axis=0)
    m6=df3.iloc[[22,23,24,25]].sum(axis=0)
    m7=df3.iloc[[26,27,28,29,30]].sum(axis=0)
    m8=df3.iloc[[31,32,33,34]].sum(axis=0)
    m9=df3.iloc[[35,36,37,38,39]].sum(axis=0)
    m10=df3.iloc[[40,41,42,43]].sum(axis=0)
    m11=df3.iloc[[44,45,46,47]].sum(axis=0)
    m12=df3.iloc[[48,49,50,51]].sum(axis=0)
    
    def new1():
        
        df2=pd.read_csv("login.csv")
        print('''


        █┼█ ███ ███ ███ █┼┼█ ███ █▄┼▄█ ███ ┼┼ ███ █┼┼█ ██▄ ┼┼ ███ ███ ███ ███ █┼┼┼█ ███ ███ ██▄
        █┼█ █▄▄ █▄┼ █▄┼ ██▄█ █▄█ █┼█┼█ █▄┼ ┼┼ █▄█ ██▄█ █┼█ ┼┼ █▄█ █▄█ █▄▄ █▄▄ █┼█┼█ █┼█ █▄┼ █┼█
        ███ ▄▄█ █▄▄ █┼█ █┼██ █┼█ █┼┼┼█ █▄▄ ┼┼ █┼█ █┼██ ███ ┼┼ █┼┼ █┼█ ▄▄█ ▄▄█ █▄█▄█ █▄█ █┼█ ███
    
        (hint paas is <channel name>123''')
        print()

        while True:
                

                
                b=input("enter your username  :")
                b1=input("enter your pass  :")
                df2.loc[5]=[b,b1]
                df2.to_csv("login.csv",index=False)
                youtube()
                break

    
    print('''select for existing user login or new user sign up''')
    print()
    print('''
a.existing user login
b.new user sign up''')
    print()
    A=input("enter your choice  :")
    print()
    if A=='a':
        print('''


        █┼█ ███ ███ ███ █┼┼█ ███ █▄┼▄█ ███ ┼┼ ███ █┼┼█ ██▄ ┼┼ ███ ███ ███ ███ █┼┼┼█ ███ ███ ██▄
        █┼█ █▄▄ █▄┼ █▄┼ ██▄█ █▄█ █┼█┼█ █▄┼ ┼┼ █▄█ ██▄█ █┼█ ┼┼ █▄█ █▄█ █▄▄ █▄▄ █┼█┼█ █┼█ █▄┼ █┼█
        ███ ▄▄█ █▄▄ █┼█ █┼██ █┼█ █┼┼┼█ █▄▄ ┼┼ █┼█ █┼██ ███ ┼┼ █┼┼ █┼█ ▄▄█ ▄▄█ █▄█▄█ █▄█ █┼█ ███
    
        (hint paas is <channel name>123''')
        print()
        df2=pd.read_csv("login.csv")

        s=pd.Series(df2["channel"])

        a11=[]
        for i in s:
            a11.append(i)


        s1=pd.Series(df2["pwd"])

        a12=[]
        for o in s1:
            a12.append(o)



        a123=input("enter username (CHANNEL NAME) : ")
        print()
        a133=input("enter password : ")
        if a123 in a11:
            if a133 in a12:
                ai12=a11.index(a123)
                ai13=a12.index(a133)
                if ai12==ai13:
                    print()              
                    home()
                
            else:
                print("Invalid pass")
                youtube()
        else:
            print("no such username exist")
            print()
            print('''
---------------------------------------------------------------------You have still not created your account-----------------------------------------------------------------------------''')
            print('''
---------------------------------------------------------------------Please sign up to create your account-------------------------------------------------------------------------------''')
            print()
            input("press enter to go back")
            new1()

    elif A=='b':
        new1()
    else:
        print("Invalid input given")
        print("give input again")
        input("press enter to go again")
        youtube()


bootup()
