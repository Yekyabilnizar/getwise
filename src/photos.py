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
    # artikel gelombang 2
    "a2-spt": ("photo-1454165804606-c3d57bc86b40", "Scott Graham", "https://unsplash.com/photos/person-holding-pencil-near-laptop-computer-5fNmWej4tAA"),
    "a2-lembur": ("photo-1567756396406-f529ebb5583d", "Blunimo Digital", "https://unsplash.com/photos/city-with-high-rise-buildings-during-night-time-Qq0tmcUrOTM"),
    "a2-negosiasi": ("photo-1758873268315-59a677aec4ba", "Vitaly Gariev", "https://unsplash.com/photos/two-colleagues-discussing-ideas-in-a-modern-office-EQJbQS0tUic"),
    "a2-anggaran": ("photo-1631511258193-252ab3da6b8b", "Sasun Bughdaryan", "https://unsplash.com/photos/a-calculator-pen-and-money-on-a-table-X4VwfPzy_2o"),
    "a2-jht": ("photo-1619149808494-d9a0a7eba166", "Mufid Majnun", "https://unsplash.com/photos/person-holding-5000-indonesian-rupiah-UAx6M-vTkos"),
    "a2-pinjam": ("photo-1688226423273-bc2f526795d5", "naufal jajuli", "https://unsplash.com/photos/a-person-holding-a-bunch-of-money-in-their-hand-gtdj9dU3u7s"),
    "a2-takeover": ("photo-1626178793926-22b28830aa30", "Towfiqu barbhuiya", "https://unsplash.com/photos/man-holding-model-house-at-desk-with-calculator-05XcCfTOzN4"),
    "a2-sbn": ("photo-1533805994737-558461dcb28e", "Nick Agus Arya", "https://unsplash.com/photos/red-and-white-flag-under-blue-sky-during-daytime-5i3oyOrojvk"),
    "a2-reksadana": ("photo-1781246435700-afec19012b45", "Ngital", "https://unsplash.com/photos/laptop-with-charts-on-a-desk-by-a-sunny-window-8OYcY9CRP_0"),
    "a2-darurat": ("photo-1607863680198-23d4b2565df0", "Andre Taissin", "https://unsplash.com/photos/pink-pig-coin-bank-on-brown-wooden-table-5OUMf1Mr5pU"),
}


def photo(key):
    pid, who, page = PHOTOS[key]
    return dict(id=pid, by=who, page=page + "?utm_source=getwise&utm_medium=referral")
