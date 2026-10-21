import csv
import sys


def main():
    if len(sys.argv) < 3:
        print('Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <x,y,wartosc> ...')
        return 1

    plik_wejsciowy = sys.argv[1]
    plik_wyjsciowy = sys.argv[2]

    try:
        with open(plik_wejsciowy, 'r', encoding='utf-8-sig', newline='') as plik:
            dane = list(csv.reader(plik))

        for zmiana in sys.argv[3:]:
            czesci = zmiana.split(',', 2)
            if len(czesci) != 3:
                print('Nieprawidłowa zmiana:', zmiana)
                print('Podaj zmianę w postaci x,y,wartosc.')
                return 1

            try:
                x = int(czesci[0])
                y = int(czesci[1])
            except ValueError:
                print('Kolumna i wiersz muszą być liczbami całkowitymi:', zmiana)
                return 1

            if y < 0 or y >= len(dane):
                print('Nie ma takiego wiersza:', y)
                return 1
            if x < 0 or x >= len(dane[y]):
                print('Nie ma takiej kolumny w podanym wierszu:', x)
                return 1

            dane[y][x] = czesci[2]

        # Wyświetlenie danych w terminalu w formacie CSV.
        csv.writer(sys.stdout, lineterminator='\n').writerows(dane)

        with open(plik_wyjsciowy, 'w', encoding='utf-8', newline='') as plik:
            csv.writer(plik).writerows(dane)

    except (OSError, UnicodeError, csv.Error) as blad:
        print('Nie udało się odczytać lub zapisać pliku:', blad)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
