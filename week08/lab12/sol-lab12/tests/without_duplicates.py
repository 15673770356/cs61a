test = {
  'name': 'without-duplicates',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (without-duplicates (list 5 4 2))
          (5 4 2)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (without-duplicates (list 5 4 5 4 2 2))
          (5 4 2)
          scm> (without-duplicates (list 5 5 5 5 5))
          (5)
          scm> (without-duplicates ())
          ()
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (without-duplicates '(5 4 3 2 1))
          (5 4 3 2 1)
          scm> (without-duplicates '(5 4 3 2 1 1))
          (5 4 3 2 1)
          scm> (without-duplicates '(5 5 4 3 2 1))
          (5 4 3 2 1)
          scm> (without-duplicates '(12))
          (12)
          scm> (without-duplicates '(1 1 1 1 1 1))
          (1)
          """,
          'hidden': False,
          'locked': False
        }
      ]
    }
  ]
}