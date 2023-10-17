import vcr

my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='fixtures',
    record_mode='once',
    match_on=['uri', 'method'],
)