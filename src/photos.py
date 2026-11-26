"""Foto latar dari Unsplash (lisensi Unsplash: bebas dipakai, kredit dicantumkan sebagai apresiasi).
Format: kunci -> (id gambar images.unsplash.com, fotografer, halaman foto)."""

PHOTOS = {
    # beranda & halaman umum
    "home": ("photo-1555899434-94d1368aa7af", "Eko Herwantoro", "https://unsplash.com/photos/selamat-datang-monument-in-jakarta-mAxA2OmTmKA"),
    "city": ("photo-1538582709238-0a503bd5ae04", "Muhammad Rizki", "https://unsplash.com/photos/glass-high-rise-buildings-during-daytime-rN3R-lKI45M"),
    "panduan": ("photo-1604594849809-dfedbc827105", "Mathieu Stern", "https://unsplash.com/photos/miniature-person-sitting-on-stack-of-coins-reading-newspaper-1zO4O3Z0UJA"),
    # kalkulator
    "pph21": ("photo-1554224155-6726b3ff858f", "Kelly Sikkema", "https://unsplash.com/photos/person-holding-paper-near-pen-and-calculator-xoU52jUVUXA"),
    "gaji-bersih": ("photo-1744957280156-ade12912ae26", "Defrino Maasy", "https://unsplash.com/photos/someone-is-holding-a-stack-of-indonesian-rupiah-L8ush_J8AnE"),
    "thr": ("photo-1779889236837-2865425674b2", "Defrino Maasy", "https://unsplash.com/photos/woven-palm-leaf-ketupat-casings-hanging-on-a-tree-trunk-Nz1ndXTjMoM"),
    "bpjs": ("photo-1623658045230-605cb00c80d6", "Mufid Majnun", "https://unsplash.com/photos/a-person-with-a-blood-pressure-meter-on-a-table-J0benOYAPbw"),
    "kpr": ("photo-1741156386380-0236c72eb6f9", "Jakub Żerdzicki", "https://unsplash.com/photos/holding-house-keys-in-front-of-the-entrance-bqUZEAeWuok"),
    "kredit-kendaraan": ("photo-1710987906260-333e7ab02b95", "Abdul Ridwan", "https://unsplash.com/photos/a-man-riding-a-motorcycle-down-a-street-filled-with-traffic-8zdLYR77uYM"),
    "deposito": ("photo-1783227610898-d53b8125c4b0", "Defrino Maasy", "https://unsplash.com/photos/a-hand-puts-indonesian-rupiah-banknotes-into-a-slot-JwyXEbShaGw"),
    "investasi": ("photo-1579621970563-ebec7560ff3e", "micheile henderson", "https://unsplash.com/photos/green-plant-on-brown-round-coins-lZ_4nPFKcV8"),
    # artikel panduan
    "a-pph21": ("photo-1709880945165-d2208c6ad2ec", "Jakub Żerdzicki", "https://unsplash.com/photos/a-calculator-sitting-on-top-of-a-table-next-to-a-laptop-8wLZi9OhsWU"),
    "a-gaji-bersih": ("photo-1625605079052-e7fcb98994ca", "Muhammad Daudy", "https://unsplash.com/photos/person-holding-a-pink-and-white-banknote-URI6ZQT0RME"),
    "a-thr": ("photo-1779889236794-b8e75f8daf82", "Defrino Maasy", "https://unsplash.com/photos/green-woven-palm-leaf-containers-for-traditional-food-6Ue7q6wsP_s"),
    "a-bpjs": ("photo-1519494026892-80bbd2d6fd0d", "Martha Dominguez de Gouveia", "https://unsplash.com/photos/hospital-lobby-reception-with-signage-nMyM7fxpokE"),
    "a-kpr": ("photo-1759428679273-11d914866394", "Jakub Żerdzicki", "https://unsplash.com/photos/hand-holding-house-keys-over-miniature-houses-t0CRdNl_mTg"),
    "a-kredit-kendaraan": ("photo-1734313519842-bab001a0cf00", "Deski Jayantoro", "https://unsplash.com/photos/a-row-of-motorcycles-parked-in-a-parking-lot-PMam6SysytM"),
    "a-deposito": ("photo-1741238700424-a979c06fe29b", "Mahen Rin", "https://unsplash.com/photos/a-pile-of-indonesian-rupiah-coins-u8OW4vCkBw8"),
    "a-investasi": ("photo-1768055105681-7d2096c5165f", "Jakub Żerdzicki", "https://unsplash.com/photos/trader-analyzing-stock-market-charts-on-multiple-screens-j_hho1mE47s"),
}


def photo(key):
    pid, who, page = PHOTOS[key]
    return dict(id=pid, by=who, page=page + "?utm_source=getwise&utm_medium=referral")
