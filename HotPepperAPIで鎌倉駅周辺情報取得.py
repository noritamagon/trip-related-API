#モジュールのインストール
import pandas as pd
import json
import requests

#取得前準備
URL="http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
API_KEY="KEY"

params={
    "key":API_KEY,
    "keyword":"鎌倉駅",
    "format":"json",
    "count":15
}

#データ取得
req=requests.get(URL,params)
result=res.json()

#スプレッドシートに転記
!pip install --upgrade gspread #スプレッドシートを操作するためのツール
!pip install --upgrade oauth2client #ドライブの情報にアクセスするためのツール
!pip install --upgrade gspread_dataframe

#アクセスの認証手続き
from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default

creds, _=default()
gc=gspread.authorize(creds)

SprSheetName="セミナー転記用"   #ブック名を定義
workbook=gc.open(SprSheetName)  #ブックを指定
worksheet=workbook.worksheet(syusai)  #シートを指定

from gspread_dataframe import set_with_dataframe
set_with_dataframe(worksheet,df,row=1,col=1,include_index=False,resize=False)