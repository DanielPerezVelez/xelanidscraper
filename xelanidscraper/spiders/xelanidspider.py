import scrapy

class XelanidSpider(scrapy.Spider):
    name = 'xelanid'
    start_urls = ['https://www.airbnb.mx/rooms/715825575916402712']

    def parse(self, response): 
        for images in response.css('div.dqra4ro.bmwtyu7.dir.dir-ltr'):
            try:
                yield {
                    'image': images.css('img.itu7ddv.i1mla2as.i1cqnm0r.dir.dir-ltr').attrib['src']
                }
            except:
                yield {
                    'image': 'no image :('
                }