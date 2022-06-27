"""
hw_01 task_01.

Написать метод domain_name, который вернет домен из url адреса.
"""


def domain_name(url: str) -> str:
    url = url.replace('//www.', '.').replace('//', '.').split('.')[1]
    return url


if __name__ == '__main__':

    assert domain_name('http://google.com') == 'google'
    assert domain_name('http://google.co.jp') == 'google'
    assert domain_name('www.xakep.ru') == 'xakep'
    assert domain_name('https://youtube.com') == 'youtube'
