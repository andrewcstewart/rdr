# Research Design Documents

`rdr` allows you to manage complex research designs through the use of Research Design Records (RDRs): small Markdown files that document key decision points in the research process.  This is facilitated through other Markdown files called ‘protocols’, which describe the processes required to determine the outcome of an RDR.  Protocols are sets of procedures that can be reused across various contexts throughout a project by serving as templates to generate reports.  Reports can take any form (Jupyter Notebooks, RMarkdown files, etc), and represent the primary substance of your research.  RDRs help impose a higher level structure of organization and navigation to the research process.


## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    rdr_project.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


