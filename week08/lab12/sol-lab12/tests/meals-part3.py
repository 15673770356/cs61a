test = {
  'name': 'meals-part3',
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
          sqlite> SELECT * FROM healthiest_meats;
          tofurky|1400
          turkey|1900
          """,
        },
      ],
    },
  ]
}