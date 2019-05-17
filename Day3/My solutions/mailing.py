# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:42:02 2019

@author: kk
"""
 # find all of the e-mail addresses on 
 # the old list that aren't on the new list. The old list is in a file 
 # containing one e-mail address per line, as in:


old_list = ["janusfury@aol.com",
"ajlitt@me.com",
"dburrows@me.com",
"robles@yahoo.com",
"jshirley@gmail.com",
"saridder@live.com",
"dmiller@mac.com",
"agapow@yahoo.ca",
"hamilton@sbcglobal.net",
"madler@att.net",
"grady@gmail.com",
"iami@gmail.com",
"heroine@gmail.com",
"loxy@att.net",
"violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]


new_list = ["violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"]

for i in old_list:
    if i not in new_list:
        print(i)
    else:
        pass 