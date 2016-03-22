import requests
import xml.etree.ElementTree as ET
from datetime import datetime

class FinnKinoXML(object):
    area_url = "http://www.finnkino.fi/xml/TheatreAreas"
    schedule_url = "http://www.finnkino.fi/xml/Schedule/"
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    def get_movies_for_area(self, area_code):
        request_url = "{}?area={}".format(self.schedule_url,
                        area_code)
        response = requests.get(request_url, headers=self.headers)
        root = ET.fromstring(response.content)
        # Check out ElementTree docs to find out how to parse
        # elements from the response data using find() and findall()
        movies = []
        for show in root.find('Shows'):
            number_of_tags = len(show)
            movie = {}
            for n in range(number_of_tags):
                tagname = show[n].tag
                tagvalue = show[n].text
                movie[tagname] = tagvalue
                #print tagname, ":", tagvalue
            #id_movie = show.find('ID').text
            movie['Picture'] = show.find('Images').find('EventMediumImagePortrait').text
            movie['TheatreAuditorium'] = show.find('TheatreAuditorium').text
            movie['PresentationMethodAndLanguage'] = show.find('PresentationMethodAndLanguage').text
            movie['OriginalTitle'] = show.find('OriginalTitle').text
            dt = datetime.strptime(show.find('dttmShowStart').text, "%Y-%m-%dT%H:%M:%S")
            movie['dttmShowStart'] = "%s:%s - %s.%s.%s" % (dt.minute, dt.hour, dt.day, dt.month, dt.year)
            dt = datetime.strptime(show.find('dttmShowEnd').text, "%Y-%m-%dT%H:%M:%S")
            movie['dttmShowEnd'] = "%s:%s - %s.%s.%s" % (dt.minute, dt.hour, dt.day, dt.month, dt.year)
            movies.append(movie)
        #return some data, e.g. a list of movie titles
        return movies
        
    def get_areas(self):
        response = requests.get(self.area_url, headers=self.headers)
        root = ET.fromstring(response.content)
        areas = {}
        
        for theatre in root.findall('TheatreArea'):
            id = theatre.find('ID').text
            name = theatre.find('Name').text
            areas[id] = name
        
        return areas
        
            