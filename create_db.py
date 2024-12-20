from app import app, db, Product

with app.app_context():
    # Veritabanını oluştur
    db.create_all()

    # Ürünler
    products = [
        # ATV Ürünleri
        Product(id=101, name="Polaris Sportsman", description="Her türlü arazi koşulunda üstün performans.", price=125000.0, city="Samsun", category="ATV", image_url="https://www.polaristurkiye.com/fileadmin/templates/model25/trim/emea/atv/spts570-ohlins-tr.jpg"),
        Product(id=102, name="Yamaha Kodiak", description="Dayanıklı ve güçlü bir ATV.", price=145000.0, city="Trabzon", category="ATV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbSxy5UqRMhoNE4n7Wp_19JLazdQdej2sPbw&s"),
        Product(id=103, name="Honda Pioneer", description="Mükemmel kontrol ve güç.", price=160000.0, city="Antalya", category="ATV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM24Xt-rqN9M_Vg7pg6T23MsZ2Q6GZ3ZasIQ&s"),
        Product(id=104, name="Can-Am Outlander", description="Arazi maceraları için tasarlandı.", price=180000.0, city="Ankara", category="ATV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUZpU2qE11gJGHUEb-fIfD3NLT2j5fmZ6_rg&s"),
        Product(id=105, name="Kawasaki Brute Force", description="Yüksek tork ve dayanıklılık.", price=150000.0, city="İstanbul", category="ATV", image_url="https://www.lectura-specs.com/models/renamed/detail_max_retina/arazi-araclari-atv-dortcekerler-brute-force-750-4x4i-kawasaki.png"),
        Product(id=106, name="CFMoto CForce", description="Modern tasarım ve teknoloji.", price=140000.0, city="Bursa", category="ATV", image_url="https://i0.shbdn.com/photos/20/37/46/x5_1204203746h5i.jpg"),
        Product(id=107, name="Suzuki KingQuad", description="Arazi koşullarında lider.", price=135000.0, city="İzmir", category="ATV", image_url="https://s1.cdn.autoevolution.com/images/moto_gallery/SUZUKI-KingQuad-700-4x4-2397_3.jpg"),
        Product(id=108, name="Arctic Cat Alterra", description="Rahat ve güvenilir.", price=120000.0, city="Muğla", category="ATV", image_url="https://arcticcat.txtsv.com/sites/default/files/_images/vehicle_page/default/1400x1050-%20600%20%281%29%20JPG-min.jpg"),
        Product(id=109, name="KTM 450 XC-F", description="Hafif ve çevik yapı.", price=160000.0, city="Adana", category="ATV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFBUzigj_N1_Fi5EH8GO1_-FzRpCcMbwsq-w&s"),
        Product(id=110, name="RZR Pro XP", description="Off-road'un lideri.", price=210000.0, city="Gaziantep", category="ATV", image_url="https://cdn.dealerspike.com/imglib/v1/800x600/imglib/Assets/Inventory/71/A3/71A35045-A4F6-405E-8124-5CCE6F65AAE1.jpg"),

        # Motosiklet Ürünleri
        Product(id=201, name="Honda CBR125", description="Performans ve ekonomi bir arada.", price=75000.0, city="İstanbul", category="Motosiklet", image_url="https://arabam-blog.mncdn.com/wp-content/uploads/2021/01/2015-cbr125r-2-repsol.jpg"),
        Product(id=202, name="Honda CBR250", description="Güçlü motor, şehir içi ve uzun yol için ideal.", price=85000.0, city="Ankara", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcUtAWuUnxn3a1XxfF6t6cRG0H4OfLQm9EVw&s"),
        Product(id=203, name="Honda CBR650", description="Yüksek hız ve stabilite.", price=125000.0, city="İzmir", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-wPgSW3hdDGMvlVe1TmiOCPgpoIbISYASlw&s"),
        Product(id=204, name="Yamaha R125", description="Başlangıç seviyesinde performans.", price=70000.0, city="Antalya", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5NmywD8sYU8k8SY4Mxdl3efRvUZzhUCsUVA&s"),
        Product(id=205, name="Yamaha R25", description="Hızlı ve şık.", price=95000.0, city="Adana", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRf9R5dodsckEwGGYujaiBOyqKncAm2-1U3Q&s"),
        Product(id=206, name="Yamaha R6", description="Profesyoneller için üstün performans.", price=180000.0, city="Bursa", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREGShehGIOdPJzxTfdOQickMaCRMthWkrkfQ&s"),
        Product(id=207, name="Yamaha R1", description="En yüksek hız ve güç.", price=250000.0, city="İstanbul", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRcnMaTNxejUi9qOtAz4MuTKGP37KyMpVICw&s"),
        Product(id=208, name="Suzuki GSX-R125", description="Hafif ve kompakt yapı.", price=80000.0, city="Samsun", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrJHiKqKAXIrDfyZsa91CshLHmFS6c4fyc_w&s"),
        Product(id=209, name="Suzuki GSX-R250", description="Yüksek hız ve konfor.", price=110000.0, city="Trabzon", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSekK3upG78KwWk8zAlL1KQHkZbjNE8kcQIA&s"),
        Product(id=210, name="Harley Davidson", description="İkonik tasarım, rahat sürüş.", price=300000.0, city="İzmir", category="Motosiklet", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs5S6wb8XYCbda4BPu7cu0gDn7pmQ_-8tPNg&s"),

        # SUV Ürünleri
        Product(id=301, name="Toyota Land Cruiser", description="Off-road'un lideri.", price=650000.0, city="İzmir", category="SUV", image_url="https://scene7.toyota.eu/is/image/toyotaeurope/2024-Land-Cruiser-Prado-First-Edition-1?wid=1280&fit=fit,1&ts=0&resMode=sharp2&op_usm=1.75,0.3,2,0"),
        Product(id=302, name="Jeep Wrangler", description="Macera dolu bir sürüş.", price=720000.0, city="Antalya", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9OFjUEbnccY2byl_qw80w3pWyI5k8v7WrbA&s"),
        Product(id=303, name="Ford Explorer", description="Rahat ve geniş iç mekan.", price=700000.0, city="Ankara", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvAE6QPTm-gtAZj8jgdEM6PUekl6y1K_7OPg&s"),
        Product(id=304, name="Chevrolet Tahoe", description="Yüksek kapasite ve performans.", price=800000.0, city="Bursa", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXDgkVkrCTlHqKCpggODQlWj8tJ3NyWJ0o1g&s"),
        Product(id=305, name="Land Rover Defender", description="Arazi sürüşünde öncü.", price=850000.0, city="İstanbul", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmwooks07hkesHt29iXfZBCWinEb8hnw1OJA&s"),
        Product(id=306, name="BMW X5", description="Lüks ve güç bir arada.", price=900000.0, city="İzmir", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3bXeVE1CMdhLnZTYD_6tBOMh4T-Pk5iRpgQ&s"),
        Product(id=307, name="Mercedes-Benz GLE", description="Şıklık ve konfor.", price=950000.0, city="Adana", category="SUV", image_url="https://media.ed.edmunds-media.com/mercedes-benz/gle-class-coupe/2025/oem/2025_mercedes-benz_gle-class-coupe_4dr-suv_amg-gle-53_fq_oem_1_1600.jpg"),
        Product(id=308, name="Audi Q7", description="Üst düzey sürüş keyfi.", price=920000.0, city="Trabzon", category="SUV", image_url="https://cdn.motor1.com/images/mgl/ojxeBq/s3/2025-audi-q7.jpg"),
          Product(id=309, name="Hyundai Palisade", description="Geniş aileler için ideal.", price=700000.0, city="Samsun", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQYgAwkrDFoMAZiKuuQ0aT7moUXyX1LVlETA&s"),
        Product(id=310, name="Kia Sorento", description="Modern tasarım ve teknoloji.", price=680000.0, city="Muğla", category="SUV", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThdgB_Cxy661J2trwXP5dKM3ujYYIgVTqTXw&s"),

        # Karavan Ürünleri
        Product(id=401, name="Volkswagen California", description="Konforlu bir karavan deneyimi.", price=950000.0, city="Muğla", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWdZFkuBryZtYTXm2wHnuzQT2lk97P97B-DQ&s"),
        Product(id=402, name="Winnebago Revel", description="Tam donanımlı lüks bir karavan.", price=1200000.0, city="Bursa", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH9aKs0L8XCXA_mqhSSst_Qrgn-i4MjBwgNw&s"),
        Product(id=403, name="Ford Transit Custom Nugget", description="Modern tasarımlı kompakt bir karavan.", price=1000000.0, city="İstanbul", category="Karavan", image_url="https://cdn.motor1.com/images/mgl/KbBpAb/s1/ford-transit-custom-nugget-2023.jpg"),
        Product(id=404, name="Hymer Grand Canyon", description="Her yolculuk için mükemmel bir seçim.", price=1400000.0, city="İzmir", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKoc0Ku0aOcM2DsNrl1CwgewhSOMaER0As0g&s"),
        Product(id=405, name="Adria Twin Supreme", description="Avrupa’nın en popüler karavanlarından biri.", price=1150000.0, city="Antalya", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHr5vrqkQes7puIm8qmVQRpNeOkm046OrKBQ&s"),
        Product(id=406, name="Mercedes-Benz Marco Polo", description="Lüks ve kompakt karavan.", price=1500000.0, city="Adana", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpF9lwCvWqNhci_K7rJIQCXQzYpamRK-0Ebw&s"),
        Product(id=407, name="Knaus Boxlife", description="Fonksiyonel bir karavan seçeneği.", price=1300000.0, city="Trabzon", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7gUmWI1LPs_E89kjLMs0MzZqDDaeB2v-hyg&s"),
        Product(id=408, name="Sunlight Cliff", description="Dayanıklı ve kompakt bir karavan.", price=900000.0, city="Samsun", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUiR-9_el8UodHLmxvWCNzzLuqu5DxHlTfnA&s"),
        Product(id=409, name="Hobby Vantana", description="Pratik bir karavan çözümü.", price=950000.0, city="Gaziantep", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGDY4EXC9Z96zTV5sKqVrnDALmTYRDdFmViQ&s"),
        Product(id=410, name="Dethleffs Globetrail", description="Yüksek kaliteli bir karavan.", price=1350000.0, city="Ankara", category="Karavan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsrrZOU6bWJH1VBc63kGDaq6caKCec0AjV2g&s"),

        # Sedan Ürünleri
        Product(id=501, name="Toyota Corolla", description="Ekonomik ve güvenilir bir sedan.", price=450000.0, city="Adana", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4DnqSZlETWGKZkZ2z9aZMQnRxH2iyj_5FFw&s"),
        Product(id=502, name="BMW 3 Serisi", description="Lüks ve performansı bir arada sunar.", price=950000.0, city="Gaziantep", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_TF1KL3_15u3sd_mB7r0XbJOEboN550nqBA&s"),
        Product(id=503, name="Mercedes-Benz C-Serisi", description="Şıklık ve kalite.", price=920000.0, city="İstanbul", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiSQLVNxYJdN1m-Rel2iBAcAakJTSpYEfUpA&s"),
        Product(id=504, name="Audi A4", description="Rahat sürüş ve modern tasarım.", price=870000.0, city="İzmir", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZD9wgVSJqALUWyTsGkdq4R1DPTop1CaMMhg&s"),
        Product(id=505, name="Honda Civic", description="Dayanıklı ve yakıt tasarruflu.", price=400000.0, city="Ankara", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQk6x3zuAR0Ek4xfI0G9Jrh0OVravm9ceueFw&s"),
        Product(id=506, name="Hyundai Elantra", description="Ekonomik bir aile aracı.", price=380000.0, city="Bursa", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiYADIWBeWU46ycXwMW0aJoFGM1D8-kLhoIQ&s"),
        Product(id=507, name="Kia Optima", description="Modern tasarım ve konfor.", price=450000.0, city="Samsun", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrS6ausf-H_ZR6sIE6aCZbywVnpjbtV0zT6Q&s"),
        Product(id=508, name="Ford Mondeo", description="Güçlü ve dayanıklı.", price=490000.0, city="Antalya", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEEugmNbLGlrG7BnJug85JZWGsEHBcEgjAUA&s"),
        Product(id=509, name="Volkswagen Passat", description="Zarif ve geniş bir sedan.", price=550000.0, city="Muğla", category="Sedan", image_url="https://cdn.motor1.com/images/mgl/NvJvM/s1/salone-di-ginevra-2019-tutte-le-novita.webp"),
        Product(id=510, name="Peugeot 508", description="Avrupa’nın popüler sedan modellerinden biri.", price=500000.0, city="Trabzon", category="Sedan", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdC1mBVaz6NGQLSmuFiHFw6k8g1NfBVoqtOA&s"),
    ]

    # Ürünleri veritabanına ekle
    db.session.add_all(products)
    db.session.commit()
    print("Tüm kategorilere 10 ürün ilan numaralarıyla birlikte başarıyla eklendi.")
