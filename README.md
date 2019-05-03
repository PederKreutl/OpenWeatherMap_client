# OpenWeatherMap klient
## Popis problému
Projekt spočíva v implementácií sieťového klienta pre prístup k serveru OpenWeatherMap. API servera poskytuje informácie o aktuálnom počasí na miestach kdekoľvek po celom svete, pričom dáta môže poskytovať v niekoľkých formátoch.  
Konkrétne bolo potrebné spracovať vstup užívateľa v podobe zadaného mesta, získať informácie o stave počasia, teplote, vlhkosti, tlaku, vetre a vypísať ich na štandardný výstup. V prípade chyby reagovať odpovedajúcim spôsobom na štandardný chybový výstup.
## Riešenie
Klienta sieťovej aplikácie som sa rozhodol realizovať v jazyku Python, nakoľko poskytuje kompaktné nástroje a vhodné moduly pre programovanie komunikácie na sieti.  
Ako prvé bolo potrebné spracovať užívateľský vstup, čo som riešil s pomocou modulu argparse. Implementáciu klienta vyžadovala použitie soketov, na čo som využil modul socket. Modul obsahuje prostriedky pre prácu so soketmi, prostredníctvom ktorých je možné komunikovať so serverom. Pre komunikáciu s API servera OpenWeatherMap bolo ďalej potrebné napísať korektný HTTP dotaz. K správnemu HTTP dotazu som sa dopracoval vďaka analýze odchytenej komunikácie v programe WireShark. V HTTP dotaze som zahrnul informáciu, aby server poslal odpoveď vo formáte JSON. Na spracovanie a vytiahnutie podstatných informácií z dát odpovedi som využil modul json. Ako posledné bolo dôležité vo výpise ošetriť situáciu, kedy server niektoré informácie neodoslal a uviesť ich ako nedostupné.
## Inštalácia a preklad
Prístup k API serveru OpenWeatherMap a teda aj korektné spustenie klienta sieťovej aplikácie vyžaduje vlastníctvo licenčného kľúča. Kľúč je možné získať po bezplatnej registrácii na webovej stránke služby OpenWeatherMap.  
Program nie je potrebné prekladať a je možné ho priamo spustiť postupom popísaným v sekcií 4.
## Spustenie
Spustenie klienta je realizované príkazom make run a je teda potrebné aby adresár obsahoval súbory Makefile a xkruty00.py. Na vstupe sú očakávané dva argumenty, prvým je API kľúč, druhým názov mesta. \
Príklad spustenia: \
    ***`$ make run api_key=<API kluc> city=<Mesto>`***
