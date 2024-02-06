# Worms and Dragons RPG
Prosta gra RPG, w której wcielasz się w bohatera wybranej klasy i walczysz ze smokami i dżdżownicami.

## Komponenty


**Enum** - 
Folder Enum zawiera definicje typów wyliczeniowych, które są wykorzystywane do reprezentowania różnych stałych i wartości w grze, takich jak rodzaje umiejętności czy typy potworów.

**Game** -
W katalogu Game znajduje się logika gry, w tym mechanizmy walki, eksploracji i postępu w grze.

**Monsters** - 
Folder Monsters zawiera definicje i charakterystyki potworów, z którymi gracze będą walczyć podczas swojej przygody.

**Player** -
Player to katalog zawierający klasy i mechanizmy zarządzania postacią gracza, w tym statystyki, ekwipunek i rozwój postaci.

**Potions** - 
W folderze Potions zdefiniowane są różne mikstury, które gracz może zbierać i używać w grze, aby pomóc sobie w różnych sytuacjach.

**Database** - W bazie danych postać użytkownika zapisuje się w kolumnie typu BLOB obiektu klasa Player. 
## Uruchomienie gry
Przed uruchomieniem należy pobrać biblioteki, wykonując polecenie w terminalu 'pip install -r requirements.txt'. Aby uruchomić grę, należy wykonać skrypt w terminalu RpgMain.py. Zapewnia on inicjalizację gry i rozpoczyna przygodę.

## Wymagania
Projekt jest zbudowany w języku Python, więc do uruchomienia gry potrzebne jest środowisko Python, najlepiej 3.10 w górę.

## Rozgrywka
1. Po uruchomieniu aplikacji użytkownik musi się zalogować, lub zarejestrować nowe konto.


2. Po zalogowaniu użytkownik musi wybrać klasę postaci.


3. Po wyborze klasy bohatera użytkownik przechodzi do swojej pierwszej walki!


4. Po stoczeniu walki użytkownik podejmuje decyzju o rozpoczęciu nowej bitwy lub zakończeniu rozgrywki.


5. Po zakończeniu rozgrywki, użytkownik może zalogować się ponownie i podjąć decyzję o kontynuowaniu sesji lub rozpoczęciu nowej.

## Autor
Anastazja Kruczek
