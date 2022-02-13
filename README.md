# BURGERZILLA
* Bu proje, hamburger restaurantlarından sipariş alan,
siparişin durumunu görüntüleyebilen, sipariş ile
ilgili müşteri/restoran yetkisinde işlemler
yapmayı sağlayan bir REST-API mikro servisidir.

## Project Details
* Müşteri; sipariş oluşturabilir, siparişin detayını görüntüleyebilir, siparişini güncelleyebilir, siparişlerini listeleyebilir ve siparişini iptal edebilir.
* Restaurant; siparişlerini listeleyebilir, siparişin detayını görüntüleyebilir, siparişi iptal edebilir, siparişin durumu ile ilgili aksiyon alabilir, menü oluşturabilir, menüye ürün ekleyebilir, menüdeki ürünleri listeleyebilir, menüden ürün silebilir, menüdeki ürünleri güncelleyebilir ve menüden ürün silebilir.
* JWT (JSON Web Token) kullanıldığı için bir müşteri başka bir müşterinin veya restaurantın bilgilerine erişemez ve müdahale edemez, aynı şekilde bir restaurantta başka bir restaurantın veya müşterinin bilgilerine erişemez ve müdahale edemez. Böylece güvenlik ihlali yaşanmaz.

## Microservices Setup and Configuration
---

## Project Layout
    📦app
    ┣ 📂api
    ┃ ┣ 📂customer
    ┃ ┃ ┣ 📜controller.py
    ┃ ┃ ┣ 📜dto.py
    ┃ ┃ ┣ 📜service.py
    ┃ ┃ ┣ 📜utils.py
    ┃ ┃ ┗ 📜__init__.py
    ┃ ┣ 📂restaurant
    ┃ ┃ ┣ 📜controller.py
    ┃ ┃ ┣ 📜dto.py
    ┃ ┃ ┣ 📜service.py
    ┃ ┃ ┣ 📜utils.py
    ┃ ┃ ┗ 📜__init__.py
    ┃ ┗ 📜__init__.py
    ┣ 📂auth
    ┃ ┣ 📜controller.py
    ┃ ┣ 📜dto.py
    ┃ ┣ 📜service.py
    ┃ ┣ 📜utils.py
    ┃ ┗ 📜__init__.py
    ┣ 📂models
    ┃ ┣ 📜customer.py
    ┃ ┣ 📜menu.py
    ┃ ┣ 📜order.py
    ┃ ┣ 📜product.py
    ┃ ┣ 📜restaurant.py
    ┃ ┣ 📜schemas.py
    ┃ ┗ 📜__init__.py
    ┣ 📜extensions.py
    ┣ 📜utils.py
    ┗ 📜__init__.py

## API Details

 * Customer ve restaurant olmak üzere iki kullanıcı var. Ayrı yetkileri olduğu için endpointleri ayrı ayrı tutulmakta.
 * Müşteriye ait; 
    - Müşteri bilgilerini alabildiği `get_customer_data` endpointi
    - Sipariş oluşturabildiği `create_orders` endpointi
    - Tüm siparişlerini alabildiği `get_orders` endpointi
    - Sipariş detaylarını alabildiği `get_order_details` endpointi
    - Siparişini güncelleyebildiği `update_order` endpointi
    - Siparişine ürün ekleyebildiği `add_product_to_order` endpointi
    - Siparişini iptal edebildiği `cancel_order` endpointi var.

* Restauranta ait;
    - Restaurant bilgilerini alabildiği `get_restauran_data` endpointi
    - Siparişlerini alabildiği `get_restaurant_orders` endpointi
    - Siparişlerinin detayını alabildiği `get_restaurant_order_details` endpointi
    - Sipariş güncelleyebildiği `update_order_status` endpointi
    - Sipariş iptal edebildiği `cancel_restaurant_order` endpointi
    - Menü oluşturabildiği `create_menu` endpointi
    - Menünün ürünlerini listeleyebildiği `get_menu_products_list` endpointi
    - Menüyü güncelleyebildiği `update_menu` endpointi
    - Menüye ürün ekleyebildiği `insert_product_to_menu` endpointi
    - Menüden ürün silebildiği `delete_product` endpointi var.



            ┣ 📂api
            ┃ ┣ 📂customer           # Müşteriye ait işlemlerin yapıldığı
                                    dosyalar bu klasör içinde yer alır.  
            ┃ ┃ ┣ 📜controller.py    # Müşteriye ait endpointler
                                    burada oluşturulur.Routlerı belirtilir ve
                                    istenilen fonksiyona ait requestler buna
                                    göre gönderilir.
            ┃ ┃ ┣ 📜dto.py
            ┃ ┃ ┣ 📜service.py       # Customer ile ilgili yapılabilecek
                                    işlemler ve customerın yetkisi olan işlemler
                                    fonksiyonlar olarak burada oluşturulur.
            ┃ ┃ ┣ 📜utils.py   
            ┃ ┃ ┗ 📜__init__.py

            ┃ ┣ 📂restaurant        # Restauranta ait işlemlerin yapıldığı
                                    dosyalar bu klasör içinde yer alır.
            ┃ ┃ ┣ 📜controller.py   # Restauranta ait endpointler
                                    burada oluşturulur.Routlerı belirtilir ve
                                    istenilen fonksiyona ait requestler buna
                                    göre gönderilir.
            ┃ ┃ ┣ 📜dto.py
            ┃ ┃ ┣ 📜service.py      # Restaurant ile ilgili yapılabilecek
                                    işlemler ve customerın yetkisi olan işlemler
                                    fonksiyonlar olarak burada oluşturulur.
            ┃ ┃ ┣ 📜utils.py
            ┃ ┃ ┗ 📜__init__.py
            ┃ ┗ 📜__init__.py

## Models Details
* Tek veritabanı üzerinde müşteri tablosu, menu tablosu, order tablosu, order item tablosu, product tablosu ve restaurant tablosu olmak üzere 6 tane tablo oluşturulmuştur.

        ┣ 📂models            # Database modelleri bu klasörde yer alır.
        ┃ ┣ 📜customer.py     # Customer tablosu oluşturulur.
        ┃ ┣ 📜menu.py         # Menu tablosu oluşturulur.
        ┃ ┣ 📜order.py        # Order tablosu oluşturulur.
        ┃ ┣ 📜product.py      # Product tablosu oluşturulur.
        ┃ ┣ 📜restaurant.py   # Restaurant tablosu oluşturulur.
        ┃ ┣ 📜schemas.py      # Hangi modelde hangi field olduğu
                                burada belirtilir.
        ┃ ┗ 📜__init__.py


## Auth Details
* Register ve Login işlemleri yapılabilmesi için iki tane endpoint burada yer alır. Müşteri ya da Restaurant olarak sistemde kayıt oluşturulabilir ve kayıt bilgileri ile giriş işlemi yapılabilir. Authentication işlemleri yapılarak email,şifre, kullanıcı kontrolleri burada yapılır.

        ┣ 📂auth             
        ┃ ┣ 📜controller.py   # Login ve Register endpointleri
                                burada yer alır. Flask tarafından gönderilen request alınır,
                                restx'e resource yapılır
        ┃ ┣ 📜dto.py          # Api'nin modelleri burada
                                oluşturulur. Hangi veriyi hangi
                                formatta alacağımız belirlitir.
                                Namespace tanımları burada yapılır.
        ┃ ┣ 📜service.py      # Veritabanı ile yapılacak işlemler
                                burada yer alır. Gerektiğinde hata mesajları gönderilir.
        ┃ ┣ 📜utils.py        # Validation işlemleri burada
                                yapılarak şifre kontrolü yapılıyor.
        ┃ ┗ 📜__init__.py


## Database ERD
 --add image!!!!!!