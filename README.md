# DailyPrint
Generate a image containing news from RSSHub



高中的时候搞的东西，因为每天需要读一些新闻积累素材写了这么个东西。

从[RSSHub](https://github.com/DIYgod/RSSHub)上获取每天的新闻然后生成一张用于打印的图片

## Features

* 自定义RSSHub地址

  将12行的`http://url_to_your_rsshub/people/opinion/223228`中`url_to_your_rsshub`替换为你的RSSHub地址，即可获取到[人民网评](http://opinion.people.com.cn/GB/223228/index.html)的内容，如有更多需要，请自行参照RSSHub的[文档](https://docs.rsshub.app/)进行修改并自行修改本项目`main.py`文件中的16-17行用于适配。

* 可生成二维码置于右上角便于访问原网址的内容。

* 自定义Logo

  修改27-32行

* 自定义字体

  修改38-40行

* 自定义版权信息

  可自行修改49行的版权信息

## Preview

*为防止版权问题，图片已做模糊化处理*

![res.png](https://i.loli.net/2021/09/17/NaF9cnrWuef84dY.png)

