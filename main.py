from vcard_parser import update_vcard_trusted_directory
from vcard_downloader import DownVcard
from vcard_uploader import UpVcard

DownVcard().download_vcard()

phone_directory_path = ["/home/adrien/Documents/PyCharm/PycharmProjects/gigaset_teldir_sync/download/teledir.vcf",
                        "/home/adrien/Documents/PyCharm/PycharmProjects/gigaset_teldir_sync/download/teledir(1).vcf",
                        "/home/adrien/Documents/PyCharm/PycharmProjects/gigaset_teldir_sync/download/teledir(2).vcf"
                        ]
trusted_directory_path = "/home/adrien/Documents/PyCharm/PycharmProjects/gigaset_teldir_sync/trusted_directory.vcf"

result = update_vcard_trusted_directory(phone_directory_path, trusted_directory_path)

print(result[0])
print(result[1])
print(result[2])

if not result[0] and not result[1]:
    print("nothing to do")
else:
    UpVcard().upload_vcard(trusted_directory_path)