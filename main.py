import scrapy

class PokeSpider(scrapy.Spider):
  name = 'pokespider'
  start_urls = ['https://pokemondb.net/pokedex/all']

  def parse(self, response):
      linhas = response.css('table#pokedex > tbody > tr')
      for linha in linhas:
      #linha = linhas[4]
        link = linha.css("td:nth-child(2) > a::attr(href)")
        yield response.follow(link.get(), self.parser_pokemon)
  
  def parser_pokemon(self,response):
    nome = response.css('main#main > h1::text')
    numero = response.css('table.vitals-table > tbody > tr:nth-child(1) > td > strong::text ')
    peso = response.css('table.vitals-table > tbody > tr:nth-child(5) > td::text')
    altura = response.css('table.vitals-table > tbody > tr:nth-child(4) > td::text')
    tipo = response.css('table.vitals-table > tbody >  tr:nth-child(2) > td > a::text')
    tipo2 = response.css('table.vitals-table > tbody >  tr:nth-child(2) > td > a:nth-child(2)::text')
    urlpag = response.url
    evolucoes = response.css('div.infocard-list-evo > div:nth-child(-n + 5) > span.infocard-lg-data.text-muted > a::text')
    evolucoesnumero = response.css('#main > div.infocard-list-evo > div:nth-child(-n + 5) > span.infocard-lg-data.text-muted > small:nth-child(-n + 5)::text')
    evolucoeslink = response.css('#main > div.infocard-list-evo > div:nth-child(-n + 5) > span.infocard-lg-data.text-muted > a::attr(href)')
    habilidadenome = response.css('div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(6) > td > span:nth-child(-n + 5) > a::text')
    habilidadelink = response.css('div:nth-child(1) > div:nth-child(2) > table > tbody > tr:nth-child(6) > td > span:nth-child(-n + 5) > a::attr(href)')

    yield{"nome": nome.get(),"numero":numero.get(),"peso": peso.get(), "altura":altura.get(), "tipos:": tipo.get(), "tipo2": tipo2.get(), "URL:": urlpag,"Evolucoes Numero:": evolucoesnumero.getall() ,"Evolucoes: ": evolucoes.getall(), "Evolucoes link:": evolucoeslink.getall(), "Habilidade nome:": habilidadenome.getall(), "Habilidade Link:": habilidadelink.getall()}

#main > div.infocard-list-evo > div:nth-child(5) > span.infocard-lg-data.text-muted > a
#     # Processa uma linha apenas
#     linha = linhas[0]

#     # Processa todas as linhas
#     for linha in linhas:

    