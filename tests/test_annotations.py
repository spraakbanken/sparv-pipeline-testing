from sparv_pipeline_testing.annotations import MockAnnotation


def test_create_empty_attributes() -> None:
    word = MockAnnotation(
        name="<token:word>",
        values=[
            "Den",
            "i",
            "HandelstidniDgens",
            "g&rdagsnnmmer",
            "omtalade",
            "hvalfisken",
            ",",
            "sorn",
            "fångats",
            "i",
            "Frölnndaviken",
            ".",
        ],
        children={"<token:word>": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]},
    )

    assert len(word.create_empty_attribute()) == 12
