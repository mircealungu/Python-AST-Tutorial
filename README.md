# Python-AST-Tutorial


computing complexity of all the python files in 
the airflow folder for example:

    find airflow -name "*.py" | xargs -L 1 python complexity.py > airflow-analysis.csv

sorting the outputs based on their complexity: 

    cat airflow-analysis.csv | sort --field-separator=',' --key=3 -n
    
    