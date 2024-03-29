extern crate cpython;
use cpython::{Python, PyResult, PyDict, py_module_initializer, py_fn};
use rand::Rng;

py_module_initializer!(libcloudtools, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust")?;
    m.add(py, "rust_version", py_fn!(py, rust_version()))?;
    m.add(py, "rust_print", py_fn!(py, rust_print(val: &str)))?;
    m.add(py, "rust_rand", py_fn!(py, rust_rand(val: &str)))?;
    Ok(())
});

fn rust_version(py: Python) -> PyResult<String> {
    const VERSION: &'static str = env!("CARGO_PKG_VERSION");
    println!("libcloudtools (ct) version: {}", VERSION);
    let sys = py.import("sys")?;
    let version: String = sys.get(py, "version")?.extract(py)?;

    let locals = PyDict::new(py);
    locals.set_item(py, "os", py.import("os")?)?;
    let user: String = py.eval("os.getenv('USER') or os.getenv('USERNAME')", None, Some(&locals))?. extract(py)?;

    println!("User: {} Python {},", user, version);
    Ok("rust_version: ".to_owned() + &version)
}

fn rust_print(_py: Python, val: &str) -> PyResult<String> {
    Ok("rust_print: cmd: ".to_owned() + val)
}

fn rust_rand(_py: Python, val: &str) -> PyResult<String> {
    let mut rng = rand::thread_rng();

    let n1: u8 = rng.gen();
    let n2: u16 = rng.gen();
    println!("Random u8: {}", n1);
    println!("Random u16: {}", n2);
    println!("Random u32: {}", rng.gen::<u32>());
    println!("Random i32: {}", rng.gen::<i32>());
    println!("Random float: {}", rng.gen::<f64>());
    Ok("rust_rand cmd: ".to_owned() + val)
}
