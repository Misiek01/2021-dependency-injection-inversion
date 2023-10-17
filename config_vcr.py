import vcr as vcrpy

vcr = vcrpy.VCR(
    path_transformer=vcrpy.VCR.ensure_suffix(".yaml"),
    cassette_library_dir="fixtures",
    record_mode="once",
    match_on=["method", "scheme", "host", "port", "path"],
)
