
from collections import deque

# ==========================================
# EXPERT SYSTEM - DIAGNOSA KERUSAKAN MOBIL
# ==========================================

rules = {
    "mesin tidak bisa menyala": "Aki bermasalah",
    "lampu dashboard redup": "Aki bermasalah",
    "suara starter lemah": "Aki bermasalah",

    "mesin cepat panas": "Sistem pendingin bermasalah",
    "air radiator berkurang": "Sistem pendingin bermasalah",
    "kipas radiator tidak berputar": "Sistem pendingin bermasalah",

    "mesin bergetar": "Busi bermasalah",
    "tarikan mesin tidak stabil": "Busi bermasalah",
    "susah dihidupkan": "Busi bermasalah"
}


# ==========================================
# SEARCH ALGORITHM - BREADTH FIRST SEARCH
# ==========================================

graph = {
    "Gejala": ["Kelistrikan", "Mesin", "Pendingin"],

    "Kelistrikan": ["Aki bermasalah"],
    "Mesin": ["Busi bermasalah"],
    "Pendingin": ["Sistem pendingin bermasalah"],

    "Aki bermasalah": [],
    "Busi bermasalah": [],
    "Sistem pendingin bermasalah": []
}


def bfs_search(start, target):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# ==========================================
# PROGRAM UTAMA
# ==========================================

print("========================================")
print(" SISTEM PAKAR DIAGNOSA KERUSAKAN MOBIL")
print("========================================")

print("\nPilih gejala yang dialami:")
print("1. Mesin tidak bisa menyala")
print("2. Lampu dashboard redup")
print("3. Suara starter lemah")
print("4. Mesin cepat panas")
print("5. Air radiator berkurang")
print("6. Kipas radiator tidak berputar")
print("7. Mesin bergetar")
print("8. Tarikan mesin tidak stabil")
print("9. Susah dihidupkan")

pilihan = input("\nMasukkan nomor gejala: ")

gejala = {
    "1": "mesin tidak bisa menyala",
    "2": "lampu dashboard redup",
    "3": "suara starter lemah",
    "4": "mesin cepat panas",
    "5": "air radiator berkurang",
    "6": "kipas radiator tidak berputar",
    "7": "mesin bergetar",
    "8": "tarikan mesin tidak stabil",
    "9": "susah dihidupkan"
}

if pilihan in gejala:

    gejala_dipilih = gejala[pilihan]

    # Expert System
    diagnosis = rules.get(gejala_dipilih)

    print("\n----------------------------------------")
    print("Gejala     :", gejala_dipilih)
    print("Diagnosis  :", diagnosis)

    # Search Algorithm
    if diagnosis == "Aki bermasalah":
        kategori = "Kelistrikan"

    elif diagnosis == "Busi bermasalah":
        kategori = "Mesin"

    elif diagnosis == "Sistem pendingin bermasalah":
        kategori = "Pendingin"

    else:
        kategori = "Gejala"

    hasil_search = bfs_search("Gejala", diagnosis)

    print("\nHasil Search Algorithm (BFS):")

    if hasil_search:
        print(" -> ".join(hasil_search))
    else:
        print("Jalur diagnosis tidak ditemukan.")

else:
    print("\nPilihan tidak valid.")
