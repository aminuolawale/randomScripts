#!/usr/bin/python3
import webbrowser

THEZEBRA = "https://www.notion.so/My-board-cf67f61b95b0481aab9236dfb619e2d9"
TURING = "https://www.notion.so/Turing-150407e8d92348fe97ca4db21c96172d"
MY_SCHEDULE = "https://www.notion.so/Schedule-42534efe9b12471caa7f79e6d80fec0c"
MY_DAILY_CHECKLIST = "https://www.notion.so/Daily-Checklist-6452da80a7d14a48b5360ce39f42e4cd"
AMMODAASTRONOMAR = "https://mail.google.com/mail/u/0/#inbox"
AMINUOLAWALEKAN = "https://mail.google.com/mail/u/1/#inbox"
chrome_path = "/usr/bin/google-chrome"
webbrowser.get(chrome_path).open(MY_SCHEDULE)
webbrowser.get(chrome_path).open(MY_DAILY_CHECKLIST)
webbrowser.get(chrome_path).open_new(THEZEBRA)
webbrowser.get(chrome_path).open(TURING)

webbrowser.get(chrome_path).open_new(AMMODAASTRONOMAR)
webbrowser.get(chrome_path).open(AMINUOLAWALEKAN)
