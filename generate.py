import time
from gen import generate_css, generate_html

if __name__ == "__main__":
    s0 = time.time()
    generate_html()
    s1 = time.time()

    t0 = time.time()
    generate_css()
    t1 = time.time()

    print("\njob complete.")
    print("\nfiles:")
    print("* thtmlx/_elements.py")
    print("* thtmlx/_elements.pyi")
    print("* thtmlx/py.typed")
    print("* thtmlx/_css.py")
    print("* gen/imports\n")
    print(f"html (w/output latency): {(s1 - s0):.2f}s")
    print(f"css  (w/output latency): {(t1 - t0):.2f}s")
