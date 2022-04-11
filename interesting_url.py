#Interesting url

# open interesting google url
import webbrowser as wb
def interesting():
	print('''CHOOSE ANY ONE OPTION\n 1 Revolving google\n2 Gravity google\n3 Roll the google\n4 Google word remover\n5 Titl google\n''')
	interesting_url=['https://therevolvinginternet.com','https://mrdoob.com/projects/chromeexperiments/google-gravity','https://www.google.com/search?gs_ssp=eJzj4tP1zc0TIo3SMmuMKoyYPQSSMIXSFRISiwqSs1RKMMrPyQEApoAKcw&q=do+a+barrel+roll&oq=do+a+&aqs=chrome.1.69i57j46i433i512j69i60j0i433i512j0i512j69i60I2j)i433i512.2553j0j9&client=ms-android-vivo&sourceid=chrome-mobile&ie=UTF-8','https://elgoog.im.zergrush/','https://www.google.com/search?q=Askew&oq=Askew&aqs=chrome..69i57j0i433i513I4j46i512j0i512I2j0i271.5339j0j9&client=ms-android-vivo&sourceid=chrome-mobile&ie=UTF-8']
	i=int(input())
	wb.open(interesting_url[i+1])
interesting()
