
```
# item au dessus de la liste avec le data-testid
x = document.querySelectorAll('[data-testid="top-sentinel"]')[1]
# donc la list
lst = x.nextElementSibling

# Récupération du nom à partir d'un item de la liste
last_item = lst.lastChild
name = last_item.firstChild.firstChild.nextElementSibling.innerText


# for loop sur la liste
out=[]
for(i=0;i<lst.children.length;i++){
    tmp = lst.children[i].firstChild.firstChild
    name = tmp.nextElementSibling.innerText
    number = tmp.innerText
    s = number + '__' + name
    out.push(s)
}
```

Là on se retrouve avec une liste de 50 items, donc c'est loadé à la volée dans cette liste

On va donc faire l'opération plusieurs fois pour mettre à jour tout ça

> voir fichier playlist.txt (loadable json)

# Recupérer l'url YT

https://www.youtube.com/results?search_query=toto

Parsing sortie avec beautiful soup en python

Objet YT html à parser
```
# second contents
<id=contents>
```
lst = idcontents
item0 = lst.firstChild
url = item0.firstChild.nextElementSibling.querySelector("a").href

> Le retour de la requete get n'est pas vrmt le meme

le Contenu de la page à l'air de se trouver dans un des champs script de la page (le 33 eme dans notre cas)

remove ça "var ytInitialData = " et le ; à la fin
> data = scripts[33].text[20:-1]
> d = json.loads(data)
>  d["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"]
> # C'est une fucking liste !!

Plus qu'a choper l'url

> (d["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]

>  d["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["videoRen
derer"]["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"]

Le second 0 est le numéro de la vidéo dans la liste des résultats


pip install youtube-dl
apt install -y ffmpeg
youtube-dl --audio-format mp3 -x http://youtube.com/watch?v=vC8qJfVYxZY

