<template>
  <div class="house" id="mainContent">

    <div class="midcontainer">

      <MenuBar />

      <div class="titlediv extraspace">
        <h1>Frequently Asked Questions</h1>
      </div>
      <div class="bodydiv">


        <div class="blurbbegin">

          <h2 class="groupHeader"> About this database</h2>



          <FaqExpandable>
            <template #header>
              Whom and what is this database for?
            </template>
            <template #default>
              <p>There has been increasing social scrutiny of the close ties between universities and the fossil fuel
                industry. For an informed discussion about whether fossil companies should be present on campus and in
                what capacity, we are documenting all current relationships between Dutch universities and these
                companies.</p>
              <p>This database can be used:</p>
              <ul>
                <li>By the <b>university administration</b>: intransparency extends to within the institution itself. Our
                  database provides policymakers and organisers within the university with the facts. While some
                  universities have already taken the first steps, a full picture allows Dutch public universities to have
                  an honest internal debate about the role of the fossil fuel industry at their institution;</li>
                <li>By <b>students and staff</b> to inform themselves about their university's fossil ties and form an
                  opinion on whether to cut these ties. This empowers them to contribute to the democratic discussions.
                  They may also compare universities, as far as transparency allows, which can help with study or
                  employment choices;</li>
                <li>By <b> investigative journalists and media outlets</b>, to use as an information source and to raise
                  public awareness of the influence of fossil fuel companies on public institutions;</li>
                <li> By <b> activist groups</b> to gain transparency around their university's ties to the fossil fuel
                  industry and to monitor the effectiveness of their activism;</li>
                <li>To raise the issue in <b> politics</b> . The influence of public institutions - research, public
                  opinion, and greenwashing to students and staff - are matters of national importance. Political parties
                  and movements fighting the fossil fuel industry's influence can use these results to inform their
                  campaigns;
                </li>
              </ul>

            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              What counts as a "fossil tie"?
            </template>
            <template #default>
              <p>We look at companies and other organisations that are active in fossil fuel (coal, oil and gas)
                extraction and enabling fossil fuel extraction (e.g. engineering and services) but not the processing of
                fossil products (e.g. Dow, BASF) or the financing of them (e.g. banks and investment funds). In
                'oil-speak' this means ‘upstream’ and ‘midstream’ activities, plus lobbying (e.g. ElementNL) and research
                (e.g. IPF Energies Nouvelles). This includes producers such as Shell, BP, Aramco, TotalEnergies, Chevron,
                ExxonMobil, ConocoPhillips as well as their daughter companies and collaborations (like NAM) but also
                companies involved in prospecting and related services, such as Schlumberger or Fugro.</p>
              <p>We do not consider chemical companies who may work with petroleum products, or other heavy industry that
                might use fossil fuels, such as Tata Steel or the aviation industry. We also do not consider other
                polluting industries such as animal agriculture and shipping.
              </p>
              <p>We look at universities (but not "<i>hogescholen</i>") in the Netherlands and at NWO, the Dutch Research
                Council. We are interested in investigating other countries in the future.</p>
              <p>We focus on fossil ties since the <a href="https://unfccc.int/process-and-meetings/the-paris-agreement"
                  target="_blank">Paris Agreement</a> in 2015, when countries committed to "pursuing efforts to limit the
                [global] temperature increase to 1.5°C", with "developed countries... taking the lead by undertaking
                economy-wide absolute emission reduction".</p>

            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              I believe some information displayed on the website is incorrect or should not be displayed here.
            </template>
            <template #default>
              <p>We check that any information passed to us can be backed up by a reliable source, and we also decide what
                to publish (weighing privacy against public interest) based on the <a href="https://www.rvdj.nl/leidraad"
                  target="_blank">Dutch Journalist Council (RvdJ) Guidelines</a>
              </p>

              <p>If you find that some information should be removed, write to us at <a
                  href="mailto:info@solid-sustainability.org">info - at - solid-sustainability.org</a>. We will
                remove the data entry while we investigate. </p>
            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              How do you ensure that privacy of academics weighs against public interest?
            </template>
            <template #default>
              <p>While professors (<i>hoogleraren</i>) and university administration (e.g. deans, board members or
                department heads) are responsible for the research projects they work on, PhD students and post-doctoral
                researchers often have little choice or influence on external funding.</p>

              <p>We therefore do not name on this website the names of academics who are not professors or do not have an
                administrative role within the university with the ability to influence funding or policy. If the
                identities of PhD students/postdocs tied to the fossil fuel industry are published on the university
                website, their identities could, of course, be found from following the links in the database. If the
                identities of these PhD students/postdocs and their link to the fossil fuel industry are not in the public
                domain, any documentation proving this link will not be published on this website.</p>

              <p>If our source for determining the tie between the professor or university administration and the fossil
                fuel company is not in the public domain (i.e. published by a reputable news source, on the university's
                own website, or the result of a FOI request), we will reach out to the person in question in accordance
                with
                the principle of fair hearing (<i>hoor en wederhoor</i>) of the <a href="https://www.rvdj.nl/leidraad"
                  target="_blank">Dutch Journalist Council (RvdJ) Guidelines</a> . Their response will be recorded in the
                relevant data entry.</p>

              <p>We will NEVER publish or link to any personal data on this website (e.g. home address, private phone
                number) that could lead to an infringement on an academics personal life, or harassment.</p>
            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              How to cite this database
            </template>
            <template #default>
              <p>Click <a @click="createBibtex">here</a> to download a Bibtex citation, and <a
                  @click="createRistex">here</a> for RIS format.</p>
              <p>In APA style you can cite us as: Mapping Fossil Ties Coalition (2023). <i>Database of Fossil Fuel
                  Industry Ties in Dutch Academia</i>. Retrieved {date}, from www.mappingfossilties.org/Database.html</p>
            </template>
          </FaqExpandable>
        </div>
        <div class="blurbBeginNoColour">


          <h2 class="groupHeader"> Why do fossil ties exist?</h2>


          <FaqExpandable>
            <template #header>
              Why do universities want to work with industry?
            </template>
            <template #default>
              <p>University researchers are often keen to enter partnerships with industry because of the access to
                funding, other resources and expertise that these bring, and the hope that topics and projects interesting
                to the company will be interesting and relevant to the industry as a whole.</p>
              <p>Collaboration with industry can also help make the step from lab tests to practical applications - an
                important consideration for researchers in science and engineering.</p>
              <p>Universities may also wish to help students with career prospects or give them insight into industry
                during a course of study, for which the university might invite companies to careers fairs or guest
                lectures. Student societies may accept financing from companies to fund their activities and the
                opportunities it may provide in the form of access to expertise and networks.</p>
            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              Why does industry want to work with universities?
            </template>
            <template #default>
              <p>Universities have a pool of researchers with expertise which can be valuable to companies, and may have
                specialised (largely publicly funded) facilities, equipment and resources that companies may not have. By
                collaborating with universities, companies may <a
                  href="https://www.chronicle.com/article/big-oil-helped-shape-stanfords-latest-climate-research-focus"
                  target="_blank">influence the research topics that are being addressed
                  towards those which benefit their business interests</a>, such as carbon capture and storage (therefore
                potentially leaving other topics unaddressed), and in addition may influence research design in a way that
                aligns with their interests.
              </p>
              <p>Universities have a good reputation for independent, reliable research, and <a
                  href="https://twitter.com/solid_research/status/1727609755483390019" target="_blank">associating with a
                  university bolsters organisations' <b>Licence to Operate</b></a>: the acceptance of their activities by
                society. Furthermore, getting research done in a university can be cheaper than at a company or other
                organisation's own R&D department.</p>
              <p>
                Universities are home to the next generation of workers: students. By collaborating with universities,
                the industry can <a
                  href="https://www.theguardian.com/environment/2022/dec/01/fossil-fuel-recruiters-banned-from-three-more-uk-universities"
                  target="_blank">identify and recruit top talent</a>. Through sponsoring student associations or giving
                bursaries, they present an image of a caring, socially-interested organisation, and depending on the
                sponsorship agreement, may have the opportunity to address students or access to student mailing lists. At
                careers events, they can present themselves as an exciting employer. And through guest lectures, they can
                influence students' learning and worldview.
              </p>

            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              Why does industry 'sponsor' professors?
            </template>
            <template #default>
              <p>Compared to other countries, Dutch universities have relatively many public-private partnerships. <a
                  href="https://fd.nl/samenleving/1468232/betaalde-hooglerarenpost-stoelpoot-voor-innovatie-maar-er-klinkt-ook-kritiek"
                  target="_blank">Research by Het Financieele Dagblad</a> (FD) revealed that of the nearly 1200 professors
                (<i>hoogleraren</i>) the FD counted, companies fund 200 of them. Philips, Shell and NXP are the biggest
                funders.
              </p>
              <p>Shell claims that the professorial positions are a matter of good employership: a researcher at Shell
                might already have contacts at a university and would like to work there part-time. If the university also
                likes the idea, a professorial chair (<i>leerstoel</i>) is opened.
              </p>
              <p>Another reason for having company employees work at a university is for the company to benefit from being
                close to new scientific insights and using these for innovation.
              </p>
              <p>Furthermore, a professorial chair provides prestiges to the company and gives legitimacy to the company's
                research.
              </p>
              <p>And ultimately, having company employees working at the university can ensure that the interests of the
                company are represented in education and research.
              </p>
              <p>The fact that professorial positions can be opened for company employees, means that there is no clear
                distinction between professors that have been promoted to that position as part of their academic career,
                and professors who have been placed in that position by third parties. Concerningly, up until recently,
                universities were <a
                  href="https://dub.uu.nl/nl/nieuws/universiteiten-geven-nieuwe-lijst-met-bijzondere-hoogleraren"
                  target="_blank">not transparent</a> about which professors are being funded by third-party funders and
                who is funding them. Due to journalist and political pressure, universities are becoming more transparent 
                on the funding of their research chairs.

              </p>
            </template>
          </FaqExpandable>

        </div>
        <div class="blurbbegin">

          <h2 class="groupHeader"> What is the debate?</h2>
          <FaqExpandable>
            <template #header>
              How could industry sponsorship of research or professors be problematic?
            </template>
            <template #default>
              <p>Through co-funding research, the fossil fuel industry can <b>influence the direction</b> that technology
                will develop and which social issues are studied. They can finance projects that are <a
                  href="https://www.imperial.ac.uk/news/128928/shell-launch-centre-imperial-research-into/"
                  target="_blank">useful for their business</a>, or fit within their business strategy. A much <a
                  href="https://www.iea.org/data-and-statistics/charts/share-of-global-capital-investment-in-selected-low-carbon-technologies-2015-2018"
                  target="_blank">higher percentage of financing</a> for Carbon Capture and Storage (CCS) comes from oil
                and gas companies than renewable technologies, because the fossil fuel industry claim that CCS allows
                future use of fossil fuels in a way that they claim to be carbon-neutral.</p>

              <p>A concerning impact of co-sponsored research is the effect on <b>scientific integrity and the risk of
                  bias</b>. In a <a href="https://www.nature.com/articles/s41558-022-01521-3"
                  target="_blank">meta-study</a>
                of research into natural gas published in Nature, a correlation was found between favourability towards
                natural gas and the funding source: research funded by the fossil fuel industry was more favourable
                towards natural gas. In the Netherlands, a <a
                  href="http://static.nrc.nl/2018/enquete-onderzoeksgeld/uitslagNederlands.pdf"> survey by a national
                  newspaper</a> found that 10% of researchers surveyed experienced unwanted pressure from companies.</p>

              <p>
                This influence of third parties, especially when it comes from fossil fuel companies, <b>undermines the
                  universities' credibility</b> as independent and that of any green ambitions or policies they have.
              </p>


              <p>In some cases, financing research is a relatively cheap form of <b>greenwashing</b>. For example,
                ExxonMobil worked with MIT, Colorado School of Mines and Michigan State University to research and promote
                biofuels made from algae, despite <a
                  href="https://theconversation.com/algal-biofuel-production-is-neither-environmentally-nor-commercially-sustainable-82095"
                  target="_blank">studies</a> showing that this solution was not scalable. Having run a successful <a
                  href="https://www.theguardian.com/environment/2021/nov/18/the-forgotten-oil-ads-that-told-us-climate-change-was-nothing"
                  target="_blank">12-year advertising campaign</a> claiming that <a
                  href="https://www.nytimes.com/paidpost/exxonmobil/algae-may-be-small-but-its-impact-could-be-big.html#100000006080550"
                  target="_blank">biofuels could power "even airplanes"</a> and that ExxonMobil planned to produce <a
                  href="https://vimeo.com/291807132" target="_blank">10,000 barrels per day</a> by 2025, ExxonMobil <a
                  href="https://www.bloomberg.com/news/articles/2023-02-10/exxon-retreats-from-major-climate-effort-to-make-biofuels-from-algae?leadSource=uverify%20wall"
                  target="_blank">stopped funding</a> for this line of research in 2023</p>


              <p>
                Publicly partnering with fossil fuel companies - the drivers of the climate crisis - can be seen to
                <b>undermine universities' stated green commitments</b>. Many Dutch universities state that they want to
                <a href="https://www.uva.nl/en/about-the-uva/about-the-university/sustainability/sustainability-at-the-uva.html"
                  target="_blank">‘be at the forefront of promoting sustainability through education and research because
                  students and academics have the potential to shape the future’</a> and that <a
                  href="https://www.uu.nl/en/research/climate-crisis" target="_blank">‘through our teaching and in our own
                  operations, climate is from now on at the forefront’</a>. Public partnerships between universities and
                fossil fuel companies contribute to greenwashing these companies’ reputations. Fossil fuel companies often
                describe their business strategy as "Paris-aligned", while continuing to invest <a
                  href="https://www.iea.org/reports/the-oil-and-gas-industry-in-energy-transitions" target="_blank">only a
                  small minority of their capital expenditure</a> in "low-carbon" technology; fossil fuels remain the <a
                  href="https://influencemap.org/EN/report/Big-Oil-s-Agenda-on-Climate-Change-2022-19585"
                  target="_blank">core of their business</a>.

              </p>
              <p>
                Universities often consider ethics when collaborating with industries, avoiding for example those involved
                in weapons and tobacco. With their core business, fossil fuel companies cause water, soil, and air
                pollution while exacerbating the climate crisis. Numerous fossil fuel multinationals have been implicated
                in <a href="https://fossilgame.org/references.html" target="_blank">human rights violations</a>; this
                alone could be a reason for universities to avoid collaboration with these companies.
              </p>
              <p>
                Finally, in many cases the research outputs of collaborative work are in the form of <b>patents</b>, or
                white papers that are not made public. For a small proportion of the research financing - the public
                resources
                make up the majority - a company can have <b>exclusive access to research results</b>.
              </p>


            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              How could invited talks or lectures be problematic?
            </template>
            <template #default>
              <p>Inviting external lectures as part of a course of study, and talks at careers events, are common practice
                in universities. For students of technical subjects, such as chemistry, physics, or engineering, speakers
                from industry can provide exciting and practical insights into problems and topics that are relevant in
                industry.</p>
              <p>However, these may be problematic for a number of reasons:</p>
              <ol>
                <li><b>One-sided information</b>: Fossil fuel companies have a vested interest in promoting the use of
                  their products and encouraging bright minds to work for them. This may lead them to provide biased
                  information, presenting themselves and their activities as attractive while ignoring the negative
                  impacts of their activities.
                </li>

                <li><b>Undermining the science</b>: The fossil fuel industry has historically <a
                    href="https://www.theguardian.com/environment/2021/nov/18/the-forgotten-oil-ads-that-told-us-climate-change-was-nothing"
                    target="_blank">been involved in efforts</a> downplay or discredit the scientific consensus on climate
                  change. While few companies now explicitly deny anthropogenic global warming, many downplay or ignore
                  its
                  severity or possible effects, or suggest that the transition away from fossil fuels <a
                    href="https://energyandcleanair.org/myth-busting-is-fossil-gas-actually-cleaner/"
                    target="_blank">should
                    be gradual</a> to avoid economic problems. </li>

                <li><b>Greenwashing</b>: Fossil fuel companies may use talks or lectures as a way to make it seem like
                  they are heavily invested in transitioning to renewables or funding relevant research. See
                  above, <b>"How could industry sponsorship of research or professors be problematic?"</b>.</li>

                <li><b>Ethical considerations</b>: Increasing numbers of students and staff consider the presence of the
                  fossil fuel
                  industry on campus as ethically problematic, as it can be seen as tacitly endorsing their actions and
                  values. Besides the ethical implications of continuing to invest in oil and gas, many such companies
                  have been implicated in <a
                    href="https://www.amnesty.org/en/latest/press-release/2017/11/investigate-shell-for-complicity-in-murder-rape-and-torture/"
                    target="_blank">human</a> <a
                    href="https://www.amnestyusa.org/chevron-found-guilty-in-8-billion-ecuadorian-human-rights-and-environmental-case/"
                    target="_blank">rights</a> abuses, for example. </li>
              </ol>


            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              How could sponsoring student organisations, career events, discussion panels etc. be problematic?
            </template>
            <template #default>
              <p>Inviting the fossil fuel industry onto campus allows them the chance to advertise amongst students. It
                can
                also be seen as a form of endorsement. For that reason, universities are starting to <a
                  href="https://dub.uu.nl/nl/achtergrond/alleen-duurzame-bedrijven-op-carrieredagen-uu"
                  target="_blank">more
                  strictly vet</a> organisations which are allowed on campus for e.g. careers events.</p>

              <p>More generally, advertising for fossil fuel industry is <a href="https://www.worldwithoutfossilads.org/"
                  target="_blank">increasingly being seen as problematic</a>; several municipalities have started to ban
                advertising for fossil fuel products and companies, and cultural institutions are increasingly declining
                sponsorship from fossil companies. Recent <a
                  href="https://open.overheid.nl/documenten/19b34bce-d4eb-4b7a-8fea-3aa9e269bf44/file"
                  target="_blank">scientific advice</a> for the Dutch Parliament concluded that a ban on fossil
                advertising is "essential but not sufficient" to effect and accelerate a sustainable transition, though
                this study focussed more on consumer products.</p>
            </template>
          </FaqExpandable>

          <FaqExpandable>
            <template #header>
              Where will the money for research come from, if not from the fossil fuel industry?
            </template>
            <template #default>
              <p>According to the <a
                  href="https://www.rathenau.nl/nl/wetenschap-cijfers/geld/wat-geeft-nederland-uit-aan-rd/financiering-en-uitvoering-van-rd-nederland"
                  target="_blank">Rathenau Institute</a>, 7.8% of Dutch university research was funded by companies in
                2021. It is not clear how much of this funding comes from the fossil fuel industry. This is because of a
                lack of transparency and disclosure from these universities. Some universities have disclosed the
                proportion of fossil funding (WUR, TUD, UU, see university summaries on the main page of this website).
                One can argue that it is the duty of the government to step in to provide funding when this is no longer
                accepted from the fossil fuel industry, especially for technology for the energy transition, which is
                evidently in the public interest.</p>
            </template>
          </FaqExpandable>
          <FaqExpandable>
            <template #header>
              What if a fossil fuel company changes direction and complies with the Paris Agreement goals?
            </template>
            <template #default>
              <p>If they would choose to, fossil fuel companies can change their core business towards renewable energy.
                An example is <a href="https://en.wikipedia.org/wiki/%C3%98rsted_(company)" target="_blank">Ørsted</a>, a
                Danish multinational energy company. Ørsted has its origin in the Danish state-owned company Dansk
                Naturgas A/S and was founded to manage gas and oil resources in the Danish sector of the North Sea. In
                2006, the company decided to focus more on green energy. Coal-fired plants were closed and oil and gas
                sites sold off, with billions of kroner reinvested in offshore wind farm technology and construction. In
                2022, 91% of
                it's heat and power were <a
                  href="https://www.statista.com/statistics/1255305/orsted-renewable-power-capacity/"
                  target="_blank">generated by renewables</a>, on track for 100% by 2025.</p>
              <p>In an <a
                  href="https://www.nrc.nl/nieuws/2023/05/17/laat-de-universiteiten-de-fossiele-industrie-nog-een-kans-geven-a4164971"
                  target="_blank">opinion piece</a>, Guus Dix and Derk Loorbach argue for a one-year moratorium on
                collaborations with the fossil industry. After a year, a committee of scientists would assess whether the
                companies covered by the moratorium are eligible for restoration, under strict conditions, or permanent
                termination of partnerships. This should be guided by the 1.5°C target of the Paris Agreement.</p>

            </template>
          </FaqExpandable>


          <FaqExpandable>
            <template #header>
              Does excluding the fossil fuel industry from research collaborations violate academic freedom?
            </template>
            <template #default>
              <p>The Encyclopaedia Britannica <a href="https://www.britannica.com/topic/academic-freedom"
                  target="_blank">defines</a> academic freedom as the freedom to teach, study and pursue knowledge and
                research without unreasonable interference or restriction. This includes free inquiry into subjects of
                their
                choosing, and no control or censorship in publishing or teaching.</p>
              <p>A lack of (financial) ties with the fossil fuel industry does not stop academics pursuing research into
                the fossil fuel industry, but would increase the freedom to research and teach without external
                interference,
                especially in research directions that would be unsupported or even opposed by the fossil fuel industry.
                Research shows that fossil fuel funding <a href="https://www.nature.com/articles/s41558-022-01521-3"
                  taget="_blank">biases research results</a>, and companies have been shown to <a
                  href="https://www.chronicle.com/article/big-oil-helped-shape-stanfords-latest-climate-research-focus"
                  target="_blank">influence the direction of research</a> in their favour (see also the question “How
                could
                industry sponsorship of research or professors be problematic?”). </p>

            </template>
          </FaqExpandable>


          <FaqExpandable>
            <template #header>
              Can academics help transform fossil fuel companies through research collaborations?
            </template>
            <template #default>
              <p>The expectation that a university could help fossil fuel companies to transform into sustainable
                corporations presupposes that these companies want to transform, which is not supported by evidence.</p>
              <p>Fossil fuel companies currently make <a
                  href="https://www.theguardian.com/business/2023/feb/07/bp-profits-windfall-tax-gas-prices-ukraine-war"
                  target="_blank">record profits with fossil fuels</a>, and have no plans to commit, in the short term, to
                the objectives of the Paris Climate Agreement. It is naive to expect them to voluntarily undermine their
                own business case.</p>
              <p>The potential impact of researchers working with a fossil fuel company is negligible, because their
                influence is very small compared to the size of the company and the number of people working there.
                Furthermore, researchers usually do not deal with the decision-makers at the top of the company. As far as
                we are aware, there has been no recorded case where researchers have managed to influence fossil fuel
                companies to take meaningful climate action.
              </p>
            </template>
          </FaqExpandable>

        </div>
        <div class="moveToMiddle"><button class="backButton" onclick="window.location.assign('./index.html')"
            type="button">Home</button>
        </div>
      </div>
    </div>


  </div>
  <footer>
    <p><b>Questions, comments or ideas for this web portal? <a class="linkDarkTheme"
          href="mailto:info@solid-sustainability.org">Contact us!</a></b></p>
    <p>© Solid Sustainability 2023</p>
  </footer>
</template>

<script>
import './assets/css/main.css';
import FaqExpandable from './components/FaqExpandable.vue';
import MenuBar from './components/MenuBar.vue'

export default {
  name: 'AppFAQ',
  components: {
    FaqExpandable,
    MenuBar
  },
  data() {
    return {
      shortUni: 'TUD',
      nameUni: 'TU Delft',
    }
  },
  methods: {
    createBibtex() {
      const stringbegin = "@techreport { mft2023 ,\n  author = { {Mapping Fossil Ties Coalition} } ,\n  year = {2023} ,\n  title = { Database of Fossil Fuel Industry Ties in Dutch Academia } ,\n  type = {} ,\n  note = { \\url{https://www.mappingfossilties.org/Database.html}, retrieved: "
      const stringend = "}\n  }"
      let date = new Date().toUTCString().slice(5, 16);
      const file = new File([stringbegin + date + stringend], 'mft.bib', {
        type: 'text/plain',
      })

      const link = document.createElement('a')
      const url = URL.createObjectURL(file)

      link.href = url
      link.download = file.name
      document.body.appendChild(link)
      link.click()

      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)

    },
    createRistex() {
      const stringbegin = "TY  - RPRT\n AU  - Mapping Fossil Ties Coalition\n TI  - Database of Fossil Fuel Industry Ties in Dutch Academia\n PY  - 2023\n DA  - 2023\n N1  - https://www.mappingfossilties.org/Database.html, retrieved: "
      const stringend = "\n ER  - "
      let date = new Date().toUTCString().slice(5, 16);
      const file = new File([stringbegin + date + stringend], 'mft.ris', {
        type: 'text/plain',
      })

      const link = document.createElement('a')
      const url = URL.createObjectURL(file)

      link.href = url
      link.download = file.name
      document.body.appendChild(link)
      link.click()

      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)

    }
  }

};

</script>

<style>
.extraspace {
  margin-bottom: 30px;
}

.groupHeader {
  font-size: 1.5em;
}</style>
