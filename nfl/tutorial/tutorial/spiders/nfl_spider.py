import scrapy

class nflspider(scrapy.Spider):
    name = 'nfl'
    start_urls = [
        'https://www.spotrac.com/nfl/rankings/2016/cap-hit.html',
        'https://www.spotrac.com/nfl/rankings/2017/cap-hit.html',
        'https://www.spotrac.com/nfl/rankings/2018/cap-hit.html'
        ]

    def parse(self, response):
        for table in response.xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/div[3]/div/table/tbody'):
            Ranking = table.css('tr td.rank.small.center.noborderright::text').extract()
            Player =  table.css('tr td.rank-name.player.noborderright h3 a.team-name::text').extract()
            Position = table.css('tr td.rank-name.player.noborderright span.rank-position::text').extract()
            CapHit = table.css('tr td span.info::text').extract()
            
        for banner in response.xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/div[3]'):
            Year = banner.css('header.team-header h2::text').extract()

            #Give the extracted content row wise
            for item in zip(Ranking,Player,Position,CapHit):
                #create a dictionary to store the scraped info
                scraped_info = {
                    'Year' : str(Year)[2:6],
                    'Ranking': item[0],
                    'Player' : item[1],
                    'Position' : item[2],
                    'Cap_Hit' : item[3]
                }
    
                #yield or give the scraped info to scrapy
                yield scraped_info

            