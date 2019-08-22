ip_address = input("Enter an IP address: ")

segment = 1
segment_length = 0
character = ''

for character in ip_address:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
if character != '.':
    print("segment {} contains {} characters".format(segment, segment_length))
