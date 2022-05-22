def generate_summary(weather_data):
    with open(weather_data, encoding="utf8") as txt_file:
        reader=csv.read(txt_file)


        def test_generate_summary_example_three(self):
        with open("tests/expected_output/example_three_summary.txt", encoding="utf8") as txt_file:
            expected_result = txt_file.read()



 expected_result = txt_file.read()
        result = weather.generate_summary(self.example_three)
        self.assertEqual(expected_result, result)