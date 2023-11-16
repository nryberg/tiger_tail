# Tiger Tail

TT is a reporting tool that lets you explore your data quickly and easily.

Data is loaded into a DuckDB database, and then queryied for patterns using a simple web interface.  You can view the data in a table or record form, search for values, and categorize the data.

There are hundreds of ways of looking at data, from there very low level CSV table viewer [CSV Kit](https://csvkit.readthedocs.io/en/latest/), through the most common tool in the world [Excel](https://www.microsoft.com/en-us/microsoft-365/excel) on up to Data Viz like [Tableau](https://www.tableau.com/).  

Each has its strengths, all come with drawbacks, whether it's cost or power. 

- CSV Look : very fast, terminal only, just text
- Excel : universal, so, so many features
- Tableau : beautiful and slow

The goal of Tiger Tail is to create static reporting, think like a blog, using a template that surfaces the data in an easy to read web page.  It'll be limited by volume, but the goal will be to focus on categories.  

## Example Data

We'll be using a playlist database.  It contains plays of holiday music from a
small selection of radio stations.  By its very nature, holiday music is limited
to just a few songs, less than a thousand typically, with the top 20% accounting
for well over 80% of plays. 

## Back End

For now, I'll be using the Hugo static site generator to create the pages - a
next step would be to migrate to an internal library that creates the final HTML
pages.  

Since the result is pretty basic anyway, it should be easy (theoretically) to
construct this.  

Templates would be:

- Home Page - some sort of landing default page
- Category - the basic group which contains a header, description (?) and an
  index.  The index is a table containing line items.
- Line Item - a table of items that fit under a Category
- Single - the most atomic unit. 

## Search

Search for high volume pages is tricky - maybe use something like [Typesense](https://typesense.org/)
- but I swear there's something else out there that's even smaller and simpler. 

## Features and Benefits

* Load data from CSV files
* Explore data using a simple table interface
* Search for values in the data


## Installation

## Usage

## Contributing

Bug reports and pull requests are welcome on [GitHub - Tiger Tail]( https://github.com/nryberg/tiger_tail). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The tool is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
