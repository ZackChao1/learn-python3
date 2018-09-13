#!/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests, time, os


# GET HTML
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"


# 处理比赛结果函数
# 采用CSS选择器过滤 class_
def print_result(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    match_list = soup.find_all('div', attrs={'class': 'matchmain bisai_qukuai'})
    for match in match_list:
        time = match.find('div', attrs={'class': 'whenm'}).text.strip()
        teamname=[]
        teamname = match.find_all('span', attrs={'class': 'team_name'})
        # 过滤注释类型
        #  if type(soup.a.string)==bs4.element.Comment: // TO DO
        # 判断无队伍名称情况

        if teamname[0].string[0:3] == 'php':
            team1_name = '暂无队名'
        else:
            team1_name = teamname[0].string

        team1_support_level = match.find('span', class_='team_number_green').string
        team2_name = teamname[1].string
        team2_support_level = match.find('span', class_='team_number_red').string

        print('比赛时间：{},\n队伍一：{}    胜率 {}\n 队伍二：{}    胜率{}\n'.format(time, team1_name, team1_support_level, team2_name,
                                                                    team2_support_level))


def main():
    url = 'http://dota2bocai.com/match'
    print_result(url)


if __name__ == '__main__':
    main()
