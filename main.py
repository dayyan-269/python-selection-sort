import pprint

data = [
  {
    'nama': "Annabell",
    'nip': "112563",
  },
  {
    'nama': "Todd",
    'nip': "142759",
  },
  {
    'nama': "Adrienne",
    'nip': "192149",
  },
  {
    'nama': "Guerrero",
    'nip': "216574",
  },
  {
    'nama': "Maya",
    'nip': "185653",
  },
  {
    'nama': "Guevara",
    'nip': "223861",
  },
  {
    'nama': "Bonner",
    'nip': "185199",
  },
  {
    'nama': "Ashley",
    'nip': "180110",
  },
  {
    'nama': "Beck",
    'nip': "158720",
  },
  {
    'nama': "Kidd",
    'nip': "212640",
  },
  {
    'nama': "Tyrese",
    'nip': "213383",
  },
  {
    'nama': "Taiba",
    'nip': "164418",
  },
  {
    'nama': "Alyce",
    'nip': "197180",
  },
  {
    'nama': "Bateman",
    'nip': "154990",
  },
  {
    'nama': "Ferne",
    'nip': "175988",
  }
]

def selection_sort(data):
    min = 0 #  variable untuk menyimpan indeks dengan nilai terkecil

    for i in range(1, len(data) - 1):
        min = i #  pada awal nilai min adalah indeks pertama
        j = i + 1

        #   perulangan untuk mencari nip terkecil
        for j in range(0, len(data)):
            if data[j]['nip'] < data[min]['nip']:
                min = j # jika iya, maka indeks akan diganti, begitu seterusnya

        #   menukarkan object sekarang dengan object yang terkecil
        data[min], data[i] = data[i], data[min]

pprint.pprint(data)
print('\n')
selection_sort(data)
pprint.pprint(data)