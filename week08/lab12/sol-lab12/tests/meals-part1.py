test = {
  'name': 'meals-part1',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab12.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM number_of_options;
          4
          """,
        },
      ],
    },
  ]
}