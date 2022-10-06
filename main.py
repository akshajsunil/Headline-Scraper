# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def main():
    # Use a breakpoint in the code line below to debug your script.
    import requests  # http req
    from bs4 import BeautifulSoup  # web scraping
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import datetime
    now = datetime.datetime.now()
    content=''

    print("akshaj is gonna start coding")

    def extract_news(url):
        print('Extracting Hacker News Stories...')
        cnt = ''
        cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
            cnt += ((str(i + 1) + ' :: ' + '<a href="' + tag.a.get(
                'href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text != 'More' else '')
            # print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
        return (cnt)
    cnt =  extract_news('https://news.ycombinator.com/')
    content = content+cnt
    content += ('<br>-------<br>')

    SERVER = 'smtp.gmail.com'
    PORT = 587
    FROM  = 'xxxxx@gmail.com'
    TO = 'xxxxxx@gmail.com'
    PASS="xxxxx"

    msg = MIMEMultipart()
    msg['Subject'] = 'Mail of the day' + str(now.day)
    msg['From'] = FROM
    msg['To'] = TO
    msg.attach(MIMEText(content,'html'))

    print('initializing the server')

    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)

    server.sendmail(FROM, TO, msg.as_string())

    print('Email Sent')
    server.quit()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
