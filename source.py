import re

file = open("source.txt",mode="r")
str=file.read()

for i in range(len(str)):
     if (i > 2 & i < 99997):
             if str[i].islower() == True:
                     if str[i-3].isupper() ==True:
                             if str[i-2].isupper() ==True:
                                     if str[i-1].isupper() ==True:
                                             if str[i+1].isupper() ==True:
                                                     if str[i+2].isupper() ==True:
                                                             if str[i+3].isupper() ==True:
								sol=(str[i-3],str[i-2],str[i-1],str[i],str[i+1],str[i+2],str[i+3])
								file2 = open("sol.txt", mode="a+")
								file2.writelines(sol)
								a="\n"
								file2.writelines(a)
                                                             else:
                                                                     pass
                                                     else:
                                                             pass
                                             else:
                                                     pass
                                     else:
                                             pass
                             else:
                                     pass
                     else:
                             pass
             else:
                     pass
     else:
             pass
