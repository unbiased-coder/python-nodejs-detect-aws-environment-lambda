function
is_aws_env()
{
    return process.env['AWS_LAMBDA_FUNCTION_NAME'] || process.env['AWS_EXECUTION_ENV'];
}

exports.handler = async (event) => {
    if (is_aws_env())
        console.log('Running inside AWS environment');
    else
        console.log('Running outside AWS environment');
};

if (!is_aws_env())
    exports.handler({});
