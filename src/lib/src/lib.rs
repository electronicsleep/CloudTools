extern crate cpython;
use cpython::{Python, PyResult, PyDict, py_module_initializer, py_fn};

py_module_initializer!(libcloudtools, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust")?;
    m.add(py, "get_version", py_fn!(py, get_version()))?;
    m.add(py, "get_result", py_fn!(py, get_result(val: &str)))?;
    m.add(py, "run_get_test", py_fn!(py, run_get_test(val: &str)))?;
    Ok(())
});

fn get_version(py: Python) -> PyResult<String> {
    let sys = py.import("sys")?;
    let version: String = sys.get(py, "version")?.extract(py)?;

    let locals = PyDict::new(py);
    locals.set_item(py, "os", py.import("os")?)?;
    let user: String = py.eval("os.getenv('USER') or os.getenv('USERNAME')", None, Some(&locals))?. extract(py)?;

    println!("User: {} Python {},", user, version);
    Ok("Python get_version: ".to_owned() + &version)
}

fn get_result(_py: Python, val: &str) -> PyResult<String> {
    Ok("Python arg: Rust val str: ".to_owned() + val)
}

fn run_get_test(_py: Python, val: &str) -> PyResult<String> {
    Ok("Python arg: val str: ".to_owned() + val)
}
