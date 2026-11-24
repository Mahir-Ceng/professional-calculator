
from decimal import Decimal, InvalidOperation

# İşlem geçmişi
history = []


# Kullanıcıdan güvenli şekilde sayı alma
def get_number(message):
    while True:
        try:
            number = Decimal(input(message))

            if not number.is_finite():
                print("Lütfen geçerli ve sonlu bir sayı girin.")
                continue

            return number

        except InvalidOperation:
            print("Hatalı giriş! Lütfen bir sayı girin.")


# Hesaplama fonksiyonu
def calculate(number1, operator, number2):

    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2

    elif operator == "*":
        return number1 * number2

    elif operator == "/":
        if number2 == 0:
            raise ZeroDivisionError("Sıfıra bölme yapılamaz.")

        return number1 / number2

    elif operator == "%":
        if number2 == 0:
            raise ZeroDivisionError("Sıfıra bölme yapılamaz.")

        return number1 % number2

    elif operator == "**":
        if number2 != number2.to_integral_value():
            raise ValueError("Üs değeri tam sayı olmalıdır.")

        if abs(number2) > 1000:
            raise ValueError("Üs değeri -1000 ile 1000 arasında olmalıdır.")

        if number1 == 0 and number2 < 0:
            raise ZeroDivisionError(
                "Sıfırın negatif kuvveti hesaplanamaz."
            )

        return number1 ** int(number2)

    else:
        raise ValueError("Geçersiz işlem operatörü.")


# İşlem geçmişini gösterme
def show_history():

    print("\n--- İŞLEM GEÇMİŞİ ---")

    if not history:
        print("Henüz işlem yapılmadı.")
        return

    for index, operation in enumerate(history, start=1):
        print(f"{index}. {operation}")


# Sayıları düzenli gösterme
def format_number(number):

    if number == 0:
        return "0"

    return format(number.normalize(), "f")


# Ana hesap makinesi
def main():

    operations = {
        "1": ("Toplama", "+"),
        "2": ("Çıkarma", "-"),
        "3": ("Çarpma", "*"),
        "4": ("Bölme", "/"),
        "5": ("Mod alma", "%"),
        "6": ("Üs alma", "**")
    }

    print("=" * 40)
    print("       PROFESSIONAL CALCULATOR")
    print("=" * 40)

    while True:

        print("\n--- İŞLEM MENÜSÜ ---")
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")
        print("5 - Mod alma")
        print("6 - Üs alma")
        print("7 - İşlem geçmişi")
        print("0 - Çıkış")

        choice = input("\nİşlem numarasını seçin: ").strip()

        # Çıkış
        if choice == "0":
            print("\nHesap makinesi kapatılıyor.")
            print("Bizi kullandığınız için teşekkürler!")
            break

        # İşlem geçmişi
        if choice == "7":
            show_history()
            continue

        # Geçersiz seçim kontrolü
        if choice not in operations:
            print("Geçersiz seçim! Lütfen 0-7 arasında seçim yapın.")
            continue

        operation_name, operator = operations[choice]

        print(f"\nSeçilen işlem: {operation_name}")

        # Sayıları al
        number1 = get_number("Birinci sayıyı girin: ")
        number2 = get_number("İkinci sayıyı girin: ")

        # Hesaplama
        try:
            result = calculate(number1, operator, number2)

            operation_text = (
                f"{format_number(number1)} "
                f"{operator} "
                f"{format_number(number2)} = "
                f"{format_number(result)}"
            )

            print("\nSonuç:", format_number(result))

            history.append(operation_text)

        except (ZeroDivisionError, ValueError, InvalidOperation) as error:
            print("\nİşlem hatası:", error)


# Programın başlangıç noktası
if __name__ == "__main__":
    main()
