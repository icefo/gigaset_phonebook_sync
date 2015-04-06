__author__ = 'adrien'


def vcard_parser(list_of_files_to_process):
    """
    :param list_of_files_to_process:
    :return: 1 list containing 1 set of vcard per input file
    """
    list_of_vcard_set = []

    for file in list_of_files_to_process:
        vcard_raw_list = set()
        # newline=None is set to automagically transform weird newlines to \n
        with open(file, encoding="utf-8", newline=None) as f:
            vcard = ""
            for line in f:
                if len(line) > 1:
                    vcard += line
                    if line.startswith("END:VCARD"):
                        vcard_raw_list.add(vcard)
                        vcard = ""
        list_of_vcard_set.append(vcard_raw_list)
    return list_of_vcard_set


def set_comparison(compared_set, reference_set):
    """
    :param compared_set:
    :param reference_set:
    :return: to_add: this is a set containing the compared_set minus the reference_set
    :return: to delete: this is a set containing the reference_set minus the compared_set
    """
    to_add = compared_set.difference(reference_set)
    to_delete = reference_set.difference(compared_set)

    return to_add, to_delete


def update_vcard_trusted_directory(list_of_directory_file_path, trusted_directory_file_path):
    """

    :param list_of_directory_file_path:
    :param trusted_directory_file_path:
    :return to_main_delete: items deleted in the trusted_directory_file
    :return to_main_add: items added in the trusted_directory_file
    :return len(trusted_set):
    """

    trusted_set = vcard_parser([trusted_directory_file_path, ])[0]

    list_of_set = vcard_parser(list_of_directory_file_path)

    to_main_delete = set()
    to_main_add = set()
    for machin in list_of_set:
        a = set_comparison(machin, trusted_set)
        to_main_add.update(a[0])
        to_main_delete.update(a[1])

    trusted_set.difference_update(to_main_delete)
    trusted_set.update(to_main_add)
    print(len(trusted_set))

    with open(trusted_directory_file_path, 'w', encoding="utf-8", newline='\r\n') as file:
        file.write("\n".join(trusted_set) + "\n")

    return to_main_delete, to_main_add, len(trusted_set)
