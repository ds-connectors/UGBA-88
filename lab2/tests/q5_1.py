test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
       'cases': [
        {
          'code': r"""
          >>> experiment_combined.num_rows == 249
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> experiment_combined.num_columns
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.mean(experiment_combined.column(5))
          2.9751457807228916
          """,
          'hidden': False,
          'locked': False
        }

      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
