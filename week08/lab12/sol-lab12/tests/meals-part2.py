test = {
  'name': 'meals-part2',
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
          sqlite> SELECT * FROM calories;
          22
          """,
        },
      ],
    },
  ]
}