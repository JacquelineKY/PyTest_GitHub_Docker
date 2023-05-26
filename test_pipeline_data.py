import pandas as pd
import pytest
import pipeline_data



def test_compute_median_mean_diff():
    # Create a test DataFrame
    test_df = pd.DataFrame({
        'Age': [20, 25, 30, 35]
    })

    # Compute the expected result manually
    expected_result = pd.DataFrame({
        'Mean_Age': [27.5],
        'Median_Age': [27.5],
        'Difference_Age': [0.0]
    })

    # Call the function with the test DataFrame
   
    result = pipeline_data.compute_median_mean_diff(test_df)
    print(result)
    print(expected_result)

    #assert expected_result['Mean_Age'] == result['Mean_Age']
    # Assert that the computed result matches the expected result
    
    pd.testing.assert_frame_equal(result, expected_result)


# Run the tests
if __name__ == '__main__':
    pytest.main()
