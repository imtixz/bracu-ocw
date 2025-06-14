export default function FilterSection() {
  return (
    <div>
      <p className="text-lg mt-2 font-bold">Filters</p>
      <div className="border p-2 px-2 border-zinc-200 mr-4 rounded my-4">
        <p className="text-lg font-bold">Department</p>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Architecture</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Business</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Biotechnology</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Computer Science & Engineering</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Economics</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Electrical Engineering</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>English</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>General Education</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Law</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Mathetmatics</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Microbiology</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Pharmacy</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Physics</p>
        </div>
      </div>
      <div className="border p-2 border-zinc-200 mr-4 rounded my-4">
        <p className="text-lg font-bold">Features</p>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Assignments</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Books</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Exams</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Lecture Videos</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Practice Problems</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Readings</p>
        </div>
        <div className="flex flex-row gap-x-2">
          <input type="checkbox" />
          <p>Slides</p>
        </div>
      </div>
    </div>
  );
}
