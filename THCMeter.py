#!/usr/bin/python3
# -*- coding: utf-8-*-
'''
MIT License THCmeter https://github.com/sourcecode347/THCMeter/

Copyright (c) 2021 Nikolaos Bazigos

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''
########################################################
# THC METER BY Nikolaos Bazigos (IMAGE METHOD)
########################################################
#http://patorjk.com/software/taag/#p=display&h=3&v=3&f=Epic&t=THC%20Meter
import numpy as np
import cv2
import random
print ('''
_________        _______    _______ _______________________ _______ 
\__   __|\     /(  ____ \  (       (  ____ \__   __(  ____ (  ____ )
   ) (  | )   ( | (    \/  | () () | (    \/  ) (  | (    \| (    )|
   | |  | (___) | |        | || || | (__      | |  | (__   | (____)|
   | |  |  ___  | |        | |(_)| |  __)     | |  |  __)  |     __)
   | |  | (   ) | |        | |   | | (        | |  | (     | (\ (   
   | |  | )   ( | (____/\  | )   ( | (____/\  | |  | (____/| ) \ \__
   )_(  |/     \(_______/  |/     \(_______/  )_(  (_______|/   \__/
                                                                    
By Nikolaos Bazigos ''')
print()

imgs=[]
THC_Results=[]
x=1
while x<=3:
	im = str(input("Enter a cannabis bud image(file path) "+str(x)+": "))
	imgs.append(im)
	x+=1
x=1
for imgx in imgs:
	img = cv2.imread(imgx)
	img = cv2.resize(img, (500, 500))
	thc = [76,174,71]	 # RGB weed color
	diff = 71
	boundaries = [([thc[2]-diff, thc[1]-diff, thc[0]-diff],
				   [thc[2]+diff, thc[1]+diff, thc[0]+diff])]

	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype=np.uint8)
		upper = np.array(upper, dtype=np.uint8)
		mask = cv2.inRange(img, lower, upper)
		output = cv2.bitwise_and(img, img, mask=mask)

		ratio_thc = cv2.countNonZero(mask)/(img.size/3)
		weed_percent = np.round(ratio_thc*100, 2)
		#print('Weed :', weed_percent ,"%")
		#cv2.imshow("THC Meter By Baz", np.hstack([img, output]))
		#cv2.waitKey(0)
	thc = [230,210,157]	 # RGB trichomes color
	diff = 25
	boundaries = [([thc[2]-diff, thc[1]-diff, thc[0]-diff],
				   [thc[2]+diff, thc[1]+diff, thc[0]+diff])]

	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype=np.uint8)
		upper = np.array(upper, dtype=np.uint8)
		mask = cv2.inRange(img, lower, upper)
		output = cv2.bitwise_and(img, img, mask=mask)

		ratio_thc = cv2.countNonZero(mask)/(img.size/3)
		trichomes_percent = np.round(ratio_thc*100, 2)
		#print('Trichomes :', trichomes_percent ,"%")
		if trichomes_percent < 0.8 and weed_percent >=10 :
			if weed_percent > 14 and trichomes_percent < 0.05:
				trichomes_percent*=random.randint(60,70)
				thc_percent = (100/weed_percent)*trichomes_percent+8
			else:
				trichomes_percent*=random.randint(60,70)
				thc_percent = (100/weed_percent)*trichomes_percent
		else:
			if weed_percent > 30 and trichomes_percent < 3:
				trichomes_percent*=(random.randint(30,38)/10)
				thc_percent = (100/weed_percent)*trichomes_percent+4
			else:
				thc_percent = (100/weed_percent)*trichomes_percent-4
		if thc_percent > 40 or thc_percent < 4:
			#print(thc_percent)
			a=1
			#print("Error : Blurred Image Or Trichomes Not Detected (!)"+str(thc_percent)+" %")
		else:
			#print('THC Of image '+str(x)+':', ("%0.2f" % thc_percent) ,"%")
			THC_Results.append(thc_percent)
			#cv2.imshow("THC Meter By Baz", np.hstack([img, output]))
			#cv2.waitKey(0)
	x+=1
def Average(lst): 
	return sum(lst) / len(lst)
print()
if len(THC_Results)>0:
	thc_average = average = Average(THC_Results)
	print ("THC : "+("%0.2f" % thc_average)+" %")
else:
	print("Error : Blurred Images Or Trichomes Not Detected (!)")
